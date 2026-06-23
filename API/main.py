from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    name:str
    age:int

@app.post("/students")
def add_student(student:Student):
    students.append(student)
    return "new student added successfully"

@app.get("/students")
def get_student():
    
    return students

@app.get("/students/{id}")
def get_student(id:int):
    return students[id]

@app.put("/students/{id}")
def update_student(id:int,student:Student):
    students[id]=student
    return "Updated Successfully"

@app.delete("/students/{id}")
def delete_student(id:int):
    if id>=len(students):
        return "Student not found"
    students.pop(id)
    return "Deleted Successfully"

[
    {
        "task_id": 101,
        "task_name": "Learning Html"
    },
    {
        "task_id": 102,
        "task_name": "Learning Python"
    },
    {
        "task_id": 103,
        "task_name": "Learning Sql"
    },
    {
        "task_id": 104,
        "task_name": "Learning Sql"
    }
]