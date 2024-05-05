from sqlmodel import SQLModel, Field

class Todo(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: int
    is_completed: bool

class UpdateTodo(SQLModel):
    title: str | None
    description: int | None
    is_completed: bool | None