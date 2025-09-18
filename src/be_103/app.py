# src/be_103/app.py
from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Alice",  "age": 22, "dept": "CSE"},
    {"id": 2, "name": "Bob",    "age": 20, "dept": "ECE"},
    {"id": 3, "name": "Charlie","age": 23, "dept": "ME"},
]

@app.route("/hello")
def hello():
    return "Hello, Interns!", 200

@app.route("/students")
def get_students():
    return jsonify(students), 200

@app.route("/")
def home():
    return "Welcome to the app!"


if __name__ == "__main__":
    app.run(debug=True)  # default port 5000

