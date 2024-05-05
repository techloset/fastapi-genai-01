from sqlmodel import SQLModel, Field

class Todos(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: int
    is_completed: bool