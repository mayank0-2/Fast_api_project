from pydantic import BaseModel

class InventoryCreate(BaseModel):

    name : str
    quantity : int
    
class InventoryUpdate(BaseModel):
    
    quantity : int
    
class InventoryBase(BaseModel):
    
    id : int
    name : str
    quantity : int
    
    class config:
        orm_mode = True