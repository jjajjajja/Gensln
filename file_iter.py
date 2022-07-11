from typing import List, Union
from sln_item import SlnItem, SlnItemType
import os 

def dive_into(root_dir: Union[str, bytes, os.PathLike]):
    header_ext = [".h", ".hpp", ".ipp", ".ixx", ".hxx"]
    source_ext = [".cpp", ".cx", ".cxx", ".c"]
    resource_ext = [".rc"]

    headers : List[SlnItem] = []
    sources : List[SlnItem] = []
    resources: List[SlnItem] = []
    filters: List[SlnItem] = []

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            file_path:str = os.path.join(subdir, file)
            file_rel_path:str = os.path.relpath(file_path, root_dir) 
            if is_header := any(map(lambda ext: file_rel_path.endswith(ext), header_ext)):
                headers.append(SlnItem(file_rel_path, SlnItemType.HEADER_FILE))
            elif is_source := any(map(lambda ext: file_rel_path.endswith(ext), source_ext)):
                sources.append(SlnItem(file_rel_path, SlnItemType.SOURCE_FILE))
            elif is_resource := any(map(lambda ext: file_rel_path.endswith(ext), resource_ext)):
                resources.append(SlnItem(file_rel_path, SlnItemType.RESOURCE_FILE))
        subdir_rel_path = os.path.relpath(subdir, root_dir)
        filters.append(SlnItem(subdir_rel_path, SlnItemType.FILTER))
    return headers, sources, resources, filters

if __name__ == '__main__':
    h,s,r,f = dive_into(R'/mnt/c/Users/jychoi/source/repos/PPW/LibraryExt/XTToolkitPro/v16.3.1/Source')
    print(len(h))
    print(len(s))
    print(len(r))
    print(len(f))