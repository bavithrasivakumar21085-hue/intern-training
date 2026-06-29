from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Task
from schemas import TaskCreate, TaskResponse
from typing import List



app=FastAPI()

@app.get("/")
def home():
   return {"message: Fastapi is Running"}

@app.post("/tasks", response_model= TaskResponse)
def add_task(task:TaskCreate, db: Session= Depends(get_db)):
    new_task = Task(title=task.title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.get("/tasks", response_model= List[TaskResponse])
def get_tasks(db: Session= Depends(get_db)):
    tasks= db.query(Task).all()
    return tasks

@app.get("/tasks/{id}", response_model= TaskResponse)
def get_task(id:int, db: Session= Depends(get_db)):
    task= db.query(Task).filter(Task.id== id).first()
    if task is None:
        raise HTTPException(
        status_code = 404,
        detail = "Task not Found"
        )
    return task

@app.put("/tasks/{id}", response_model= TaskResponse)

def update_task(id:int, task: TaskCreate, db: Session= Depends(get_db)):

    existing_task = db.query(Task).filter(Task.id==id).first()

    if existing_task is None:
        raise HTTPException(
            status_code =404,
            detail = "Task not found"
        )
    existing_task.title = task.title
    db.commit()
    db.refresh(existing_task)
    return existing_task


@app.delete("/tasks/{id}")
def delete_task(id:int, db: Session= Depends (get_db)):
    existing_task= db.query(Task).filter(Task.id==id).first()
    if existing_task is None:
        raise HTTPException(
            status_code= 404,
            detail="Task not found"
        )
    db.delete(existing_task)
    db.commit()
    return "Task Deleted Successfully"