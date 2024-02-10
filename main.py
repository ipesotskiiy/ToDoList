from typing import List

from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.models import ToDo
from schemas import ToDoCreateSchema, ToDoSchema

app = FastAPI()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.post('/todo', response_model=ToDoSchema, status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDoCreateSchema, session: Session = Depends(get_session)):
    tododb = ToDo(task=todo.task)
    session.add(tododb)
    session.commit()
    session.refresh(tododb)
    return tododb


@app.get('/todo/{id}', response_model=ToDoSchema)
def read_todo(id: int, session: Session = Depends(get_session)):
    todo = session.query(ToDo).get(id)

    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo


@app.get('/todo', response_model=List[ToDoSchema])
def read_todo_list(session: Session = Depends(get_session)):
    todo_list = session.query(ToDo).all()
    return todo_list


@app.put('/todo/{id}')
def update_todo(id: int, task: str, session: Session = Depends(get_session)):
    todo = session.query(ToDo).get(id)

    if todo:
        todo.task = task
        session.commit()

    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo


@app.delete('/todo/{id}')
def delete_todo(id: int, session: Session = Depends(get_session)):
    todo = session.query(ToDo).get(id)
    if todo:
        session.delete(todo)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return f'ToDo object with the id {id} was successfully deleted'
