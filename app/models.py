from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    
class Loader (BaseModel):
    filePath: str
    
class Query(BaseModel):
    query: str
    neighbours: Optional[int] = 3