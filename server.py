from fastapi import FastAPI,Query,Path,HTTPException
from pydantic import BaseModel,Field,computed_field
import json
from typing import List,Dict,Annotated,Literal,Optional
from fastapi.responses import JSONResponse
app = FastAPI()

class updatePatient(BaseModel):
    name:Annotated[Optional[str], Field(default=None)]
    city:Annotated[Optional[str], Field(default=None)]
    age:Annotated[Optional[int], Field(default=None, gt=0, lt =
70)]
    gender:Annotated[Optional[str], Field(default=None)]
    height:Annotated[Optional[float], Field(default=None, gt=0)]
    weight:Annotated[Optional[float], Field(default=None, gt=0)]

class Patient(BaseModel):
    id:Annotated[str, Field(..., description="unique patient id",example="P001")]
    name:Annotated[str, Field(..., description="patient name ", example ="Dhruta")]
    city:Annotated[str, Field(..., description="patient city", example = "mumbai")]
    age:Annotated[int, Field(..., description="patient age", example = 25, gt=0, lt = 70)]
    gender:Annotated[str, Field(..., description="enter gender")]
    height:Annotated[float, Field(..., description="patient height", example = 174.3 ,gt=0)]
    weight:Annotated[float, Field(..., description="patient weight", example = 74.3 ,gt=0)]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)-> str:
        if self.bmi < 18.5:
            return "underweight"
        elif 18.5 <= self.bmi <25:
            return "Healty"
        elif self.bmi >=25:
            return "overweight"
        else:
            return "obese"

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data,f)


@app.get("/")
def home():
    return {"message": "patient management system APIs"}

@app.get("/view")
def view_patient():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def patient(patient_id:str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, details = "patient not found")


@app.get("/sort")
def sort_patient(
    sort_by: str = Query(..., description="sort by weight or age or height"),
    order: str = Query('asc', description="sort in asc or desc order")
):
    valid_fields = ["age","weight","height"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, details=f"invalid select from {valid_fields}")
    if order not in['asc','desc']:
        raise HTTPException(status_code=400, details="order must be 'asc' or 'desc'")
    
    data = load_data()
    patients = list(data.values())
    reverse = True if order == 'desc' else False
    sorted_patients = sorted(patients, key=lambda x: x[sort_by], reverse=reverse)
    return sorted_patients


@app.post("/add")
def add_patient(patient : Patient):

    #load existing data
    data = load_data()
    #check if patient already exists
    if patient.id in data:
        raise HTTPException(status_code = 400, detail="patient already exists")
    
    #new patient add to DB
    data[patient.id] = patient.model_dump(exclude=["id"])

    #save with new patient detail in json file
    save_data(data)

    return JSONResponse(status_code = 201, content={"message": "patient added successfully"})

@app.put("/update/{patient_id}")
def update_patient(patient_id:str , patient_update: updatePatient):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code = 404, detail = "patient not found")
    existing_patient = data[patient_id]
    update_patient_info = patient_update.model_dump(exclude_unset=True)
    for key, value in update_patient_info.items():
        existing_patient[key] = value
    # existing_patient -> pydantic_class -> update bmi + verdict ->pydantic obj -> dict
    existing_patient['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient)
    data[patient_id] = patient_pydantic_obj.model_dump(exclude=['id'])

    #save model
    save_data(data)
    return JSONResponse(status_code = 200, content={"message": "patient updated successfully"})


@app.delete("/delete/{patient_id}")
def delete_patient(patient_id:str):
    #load data
    data = load_data()

    if patient_id not in data:
        HTTPException(status_code = 404, details = "patient not found")
    
    #delete patient
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={"message": "patient deleted successfully"})
