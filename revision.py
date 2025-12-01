from fastapi import FastAPI
app = FastAPI()
import sqlite3

DB = "student.db"

students={
    1: {"name": "Dhruta", "course":"BT"},
    2: {"name":"saloni","course":"CSE"}
}
@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_students_id(student_id:int):
    return students.get(student_id, "error found no such student exist")

@app.post("/students")
def add_students(student_id:int,name:str,course:str):
    if student_id in students:
        return{"error":"user already exist"}
    students[student_id] = {"name":name , "course":course}
    return {"message":"new user created","data":students[student_id]}
@app.put("/students/{student_id}")
def update_students(student_id:int,name:str,course:str):
    if student_id not in students:
        return {"error":"student not found"}
    students[student_id] = {"name":name, "course":course}
    return {"message":"student updated","data":students[student_id]}

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return{"message":"student cant be deleted"}
    delete = students.pop(student_id)
    return {"message":"student successfully deleted","delelted_item":delete}