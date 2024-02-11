from pydantic import BaseModel


class ToDoCreateSchema(BaseModel):
    task: str


class ToDoSchema(BaseModel):
    id: int
    task: str

    class ConfigDict:
        from_attributes = True
