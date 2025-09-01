from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"message": "Welcome to my first fastAPI"} 

@app.get("/items/{item_id}")
def read_item(item_id:int):
    return {"item_id": item_id}

@app.get("/search")
def search_item(q: str = None, limit: int = 10):
    return {"q": q}  

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return {"received_item": item, "message": "Item created successfully"}
    
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "item_id": item_id,
        "updated_item": item,
        "message": "Item updated successfully"
    }
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item with id {item_id} deleted successfully"}