from fastapi import FastAPI, status, HTTPException
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


@app.get('/todo/{id}')
def read_todo(id: int):
    session = Session(bind=engine, expire_on_commit=False)
    todo = session.query(ToDo).get(id)
    session.close()

    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo


@app.get('/todo')
def read_todo_list():
    session = Session(bind=engine, expire_on_commit=False)
    todo_list = session.query(ToDo).all()
    session.close()
    return todo_list

