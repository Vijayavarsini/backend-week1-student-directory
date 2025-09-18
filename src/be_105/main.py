# src/be_105/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Student Directory API (Week 1)")

class Student(BaseModel):
    id: int
    name: str
    age: int
    dept: str

# in-memory dataset
students_db = [
    Student(id=1, name="Alice",  age=22, dept="CSE"),
    Student(id=2, name="Bob",    age=20, dept="ECE"),
    Student(id=3, name="Charlie",age=23, dept="ME"),
    Student(id=4, name="Disha",  age=21, dept="CSE"),
]

@app.get("/students", response_model=List[Student])
def list_students():
    return students_db

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for s in students_db:
        if s.id == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")
