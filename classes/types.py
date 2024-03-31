class Car(BaseModel):
    id:int | str
    color:str = "any default titile value"
    details: Optional[str] = "any default"
    


@app.post("/verify-image")
async def verif_image(img=None):
   output =await ModelA(img)


userName: Annotated[int,23,"saf",Path(ge=10)] = "naveedsarwar"
age:int = 25
0101
listOfStudentNames:list[str] = ["First", "Second", "Third"]
car:dict[str, int]= {
    "id": 2025,
    "title":"red",
    "description": "any description"
    
}

def getUserFullName(firstName:str | None  = None, lastName:str = None, age:int = None):
    return firstName + " " + lastName
