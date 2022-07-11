from gen_filter_xml import gen_filter_xml
from file_iter import dive_into

path = R'/mnt/c/Users/jychoi/source/repos/PPW/LibraryExt/XTToolkitPro/v16.3.1/Source'

headers, sources, resources, filters = dive_into(path)

gen_filter_xml('test.filter', filters, headers, sources)