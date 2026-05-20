from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import models , schema

router = APIRouter()

db = SessionLocal()

@router.post("/employees/")
async def create_new_employee(employee : schema.employeecreate):
    new_employee = models.Employee(
        name = employee.name,
        age = employee.age,
        salary = employee.salary
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee

@router.get("/employees/{employee_id}")
async def get_emplyees(employee_id : int):
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()
    if employee is None:
        raise HTTPException(
            status_code = 404,
            detail = "employee not found"
        )
    return employee

@router.get("/employees/")
async def get_all_employees():
    employees = db.query(models.Employee).all()
    return employees

@router.put("/employee/{employee_id}")
async def update_employee(employee_id : int , updated_employee : schema.employeecreate):
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()
    if employee is None:
        raise HTTPException (
            status_code = 404,
            detail = "user not found"
        )
    employee.name = updated_employee.name
    employee.age = updated_employee.age
    employee.salary = updated_employee.salary

    db.commit()

    return{
        "message" : "employee updated"
    }

@router.delete("/employee/{employee_id}")
async def delete_empoyee(employee_id:int):
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()
    if employee is None:
        raise HTTPException(
            status_code = 404,
            detail = "user not found"
        )
    db.delete(employee)
    db.commit()
    return {
        "message" : "user deleted successfully"
    }
