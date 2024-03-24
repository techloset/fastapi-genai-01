from fastapi import FastAPI
import uvicorn

app = FastAPI()

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

@app.get("/addStudent")
def addStudent(userName:str, rollNo:str):
    global students
    students.append({"userName":userName, "rollNo":rollNo})
    return students

@app.get("/")
def helloWorld():
    return {"hello": "world"}

@app.get("/gettodos/{userName}/{rollNo}")
def getTodos(userName:str, rollNo:str):
    print("Get todos called",userName,rollNo)
    return userName + rollNo 

@app.post("/gettodos")
def getTodosPost():
    print("Get post method todos called")
    return "post gettodos called"

@app.get("/getSingleTodo")
def getSingleTodo(userName:str, rollNo:str):
    print("Get todo called",userName,rollNo )
    return "getSingleTodo called sadf sd sdff"

@app.put("/updateTodo")
def updateTodo():
    return "updateTodo called"
    

def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)




