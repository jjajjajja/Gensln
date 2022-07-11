from enum import Enum

class SlnItemType(Enum):
    FILTER = 1 
    SOURCE_FILE = 2
    HEADER_FILE = 3
    RESOURCE_FILE = 4
    
class SlnItem:
    path : str 
    type : SlnItemType
    
    def __init__(self, path: str, type: SlnItemType):
        self.path = path 
        self.type = type


