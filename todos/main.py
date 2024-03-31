from fastapi import FastAPI, Body, Query, Path
import uvicorn
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    id:int 
    title:str
    description : str

class User(BaseModel):
    userName:str = Field(max_length= 10)
    
@app.get("/students/{id}")
def MainRoute(id:Annotated[int, Path(le=5, ge =3)]):
    return id   


@app.post("/students")
def MainRoute(item:Item, user:User, count:Annotated[int, Body()]):
    print(user)
    return item   

# @app.get("/students")
# def MainRoute(item_sf:Annotated[str, Query(title="saf", description="Sf", alias="item-test",max_length=10, min_length=4, pattern="^fix[a-zA-Z0-9]")]):
#     return item_sf   

def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)




