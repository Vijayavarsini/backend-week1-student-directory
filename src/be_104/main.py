from fastapi import FastAPI

app = FastAPI(title="BE-104 FastAPI Basics")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    # dummy data
    return {
        "id": student_id,
        "name": f"Student {student_id}",
        "age": 18 + (student_id % 6),
        "dept": "CSE"
    }
