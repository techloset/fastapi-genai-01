from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def helloWorld():
    return "Hello, world!"

@app.get("/gettodos")
def getTodos():
    print("Get todos called")
    return "gettodos called"

@app.post("/gettodos")
def getTodosPost():
    print("Get post method todos called")
    return "post gettodos called"

@app.get("/getSignleTodo")
def getSingleTodo():
    print("Get todo called")
    return "getSingleTodo called sadf sd sdff"

@app.put("/updateTodo")
def updateTodo():
    return "updateTodo called"
    

def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)


