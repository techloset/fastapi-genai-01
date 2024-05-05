from fastapi import FastAPI, HTTPException
import uvicorn
from sqlmodel import Session, select
from dotenv import load_dotenv
load_dotenv()

from .models.todos import Todo, UpdateTodo
from .config.db import create_tables, engine

app = FastAPI()


@app.get("/get_todos")
def get_todos():
    with Session(engine) as session:
        statement = select(Todo)
        results = session.exec(statement)
        data = results.all()
        print(data)
        return data


@app.put("/update_todo/{id}")
def update_todo(todo: UpdateTodo):
    with Session(engine) as session:
        db_todo = session.get(Todo, id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        todo_data = todo.model_dump(exclude_unset=True)
        db_todo.sqlmodel_update(todo_data)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return {"status": 200, "message": "todo updated successfully"}


@app.post("/create_todo")
def create_todo(todo: Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return {"status": 200, "message": "todo created successfully"}


@app.delete("/delete_todo/{todo_id}")
def delete_todo(todo_id):
    with Session(engine) as session:
        print(todo_id)
        db_todo = session.get(Todo, int(todo_id))
        print(db_todo)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        session.delete(db_todo)
        session.commit()
        session.refresh(db_todo)
        return  {"status": 200, "message": "todo deleted successfully"}


def start():
    create_tables()
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8080, reload=True)
