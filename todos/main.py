from fastapi import FastAPI
import uvicorn
from sqlmodel import Session, select
from dotenv import load_dotenv
load_dotenv()

from .config.db import create_tables, engine
from .models.todos import Todos


app = FastAPI()

@app.get("/get_todos")
def get_todos():
    with Session(engine) as session:
        statement = select(Todos)
        results = session.exec(statement)
        data = results.all()
        print(data)
        return data

def start():
    create_tables()
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)