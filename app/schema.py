from pydantic import BaseModel

class employeecreate(BaseModel):
    name : str
    age : int
    salary : float

class employeeresponse(employeecreate):
    id : int

    class Config:
        orm_mode = True