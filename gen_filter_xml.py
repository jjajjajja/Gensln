from typing import Dict, List
from mindom_helper import xmlchild
from xml.dom import minidom
from uuid import uuid4
from sln_item import SlnItem, SlnItemType
import os

def gen_filter_xml(output_name : str, filters: List[SlnItem], includes: List[SlnItem], sources : List[SlnItem]):
    doc = minidom.Document()
    with xmlchild(doc, 'Project') as proj:
        group_type = ['Filter', 'ClInclude', 'ClCompile']
        for type in group_type:
            with xmlchild(proj, 'ItemGroup') as item_group:
                if type == 'Filter':
                    for f in filters: 
                        with xmlchild(item_group, type) as elem:
                            elem['Include'] = f.path
                            with xmlchild(elem, 'UniqueIdentifier') as uid:
                                uid.text = f'{{{uuid4()}}}'
                elif type == 'ClInclude' or  type == 'ClCompile':
                    iters = includes if type == 'ClInclude' else sources
                    for i in iters:
                        with xmlchild(item_group, type) as elem:
                            elem['Include'] = i.path
                            with xmlchild(elem, 'Filter') as f:
                                f.text = os.path.dirname(i.path)
    with open(output_name, 'wb') as f:
        f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))


if __name__ == '__main__':
    gen_filter_xml('example.vcxproj.filters')