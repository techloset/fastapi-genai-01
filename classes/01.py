from fastapi import FastAPI, Path, Query, Body
import uvicorn
from pydantic import BaseModel
from typing import Annotated


class Todo(BaseModel):
    title:str | None
    description: str
    
    
@app.post("/todos/{id}")
def todos(id: Annotated[int, Path(title="id path variable taking int variable", ge=20, le=50)], item: Annotated[str | None, Query(max_length=20)] = "SDF", data:Todo | None = None, count:Annotated[int, Body()] = 10):
    print(data)
    return data
    

students = [{
    "userName":"Ali",
    "rollNo": 2342
},
            {
    "userName":"Naveed Sarwar",
    "rollNo": 9213
}
            ]

@app.get("/students")
def getStudents():
    return students


    

@app.get("/students/{rollno}")
def getFilteredStudents(rollno):
    print(rollno)
    filteredStudents = list(filter( lambda item: item["rollNo"] == int(rollno),students))
    print(filteredStudents)
    
    return filteredStudents


@app.post("/students")
def createStudent(rollno, username, todo):
    global students
    students.append({"rollNo":int(rollno), "username":username})
    return "Student created"

def updateStudents(student):
    if student["rollNo"] == 9213:
        return {
            "rollNo": 9213,
            "username":"abc"
        }
    else:
      return student
        

@app.put("/students/{rollno}")
def updateStudent(rollno, username):
    global students
    updatedStudentsRecord = list(map(updateStudents,students))
    print(updatedStudentsRecord)
    students = updatedStudentsRecord
    return "Student updated"
    