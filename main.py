from fastapi import FastAPI, status
from sqlalchemy.orm import Session

from database import engine
from models.models import ToDo
from schemas import ToDoRequest

app = FastAPI()


@app.post('/todo', status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDoRequest):
    session = Session(bind=engine, expire_on_commit=False)
    tododb = ToDo(task=todo.task)
    session.add(tododb)
    session.commit()
    id = tododb.id
    session.close()
    return f"created todo item with id {id}"
