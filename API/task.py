from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
tasks = []

class Tasks(BaseModel):
    task_id: int
    task_name: str


@app.post("/task")
def add_task(task: Tasks):
    tasks.append(task)
    return {"message": "Task added successfully"}


@app.get("/task")
def get_tasks():
    return tasks


@app.get("/task/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task_id == task.task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.put("/task/{task_id}")
def update_task(task_id: int, updated_task: Tasks):
        for index, task in enumerate(tasks):
            if task_id == task.task_id:
                tasks[index]= updated_task
            return {
                "message": "Task updated successfully",
                "task": updated_task
            }

        raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.delete("/task/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task_id == task.task_id:
            tasks.remove(task)
            return {
                "message": "Task deleted successfully",
                }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )