from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app=FastAPI()
tasks=[]

class Tasks(BaseModel):
    title: str

@app.post("/tasks")
def add_task(task:Tasks):
    tasks.append(task)
    return "Task added Successfully"

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task(id:int):
    if id >= len(tasks):
        raise HTTPException(
        status_code = 404,
        detail = "Task not Found"
        )
    return tasks[id]

@app.put("/tasks/{id}")
def update_task(id:int, task:Tasks):
    tasks[id]=task
    if id >= len(tasks):
        raise HTTPException(
            status_code =404,
            detail = "Task not found"
        )
    return "Task Updated"


@app.delete("/tasks/{id}")
def delete_task(id:int):
    tasks.pop(id)
    if id >= len(tasks):
        raise HTTPException(
            status_code= 404,
            detail="Task not found"
        )
    return "Task deleted successfully"