from typing_extensions import Self
from xml.dom.minidom import Document, Element
from typing import Union

class ChildXmlElementWrapper:
    parent : Union[Document, Self]
    child : Element

    # built-in method overloading...
    def __init__(self, parent, child_name):
        self.parent = parent
        self.child = Document().createElement(child_name)
    def __enter__(self):
        return self
    def __exit__(self,a,b,c):
        self.parent.appendChild(self.child)
        return
    def __getitem__(self, key):
        return self.child.getAttribute(key)
    def __setitem__(self, key, value):
        self.child.setAttribute(key, value)

    # minidom.Document compatible api 
    def appendChild(self, child): # for document compatiblity
        return self.child.appendChild(child)

    @property
    def text(self):
        return self.child.nodeValue
    @text.setter
    def text(self, value):
        text_node = Document().createTextNode(value)
        self.child.appendChild(text_node)

def xmlchild(parent : object, child_name: str): return ChildXmlElementWrapper(parent, child_name)
