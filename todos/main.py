from fastapi import FastAPI
import uvicorn
from sqlmodel import SQLModel,Session, Field, create_engine,select


app = FastAPI()
connection_string = 'postgresql://postgres.mvywpktaqokwusajghbz:Jc.UDqZ!nLv7MN$@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres'
connection = create_engine(connection_string)

class Students(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    name: str
    age: int
    is_active: bool
    
    
SQLModel.metadata.create_all(connection)


@app.get("/getStudents")
def getStudents():
    with Session(connection) as session:
        statement = select(Students).where(Students.id == 1)
        results = session.exec(statement)
        data = results.all()
        print(data)
        return data



def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)


# select(Students) == select * from students;





# from fastapi import FastAPI, Body, Query, Path
# import uvicorn
# from sqlmodel import Field, Session, SQLModel, create_engine, select # type: ignore

# # SAME CODE AS ABOVE
# app = FastAPI()
# url = f'postgresql://postgres.mvywpktaqokwusajghbz:Jc.UDqZ!nLv7MN$@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres'
# connection = create_engine(url)


# class Hero(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str
#     secret_name: str
#     age: int | None = None
    
# SQLModel.metadata.create_all(connection)

    
# @app.get("/heroes/")
# def get_heroes():
#     with Session(connection) as session:
#         statement = select(Hero).where(Hero.age <= 35)
#         results = session.exec(statement)
#         return results.all()
            
# def start():
#     uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)




