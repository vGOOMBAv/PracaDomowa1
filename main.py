# main.py
 
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from flask import Flask

class Item(BaseModel):
	name:str
	surename:str

class Patient():
    name:str
    surename:str
    id:int
    def __init__(self, name_e:str, surename_e:str, id_e:int):
        self.name=name_e
        self.surename=surename_e
        self.id=id_e

app = FastAPI()
app.counter=0
app.patient_list=[1,2,3]

@app.get("/")
def root():
    return {"message": "Hello World"}
 
@app.get("/patient/{id}")
def return_patient_data(id):
    is_patient=False
    patient_pos=0
    for i in range(app.patient_list.len()):
        if(app.patient_list[i].id==id):
            is_patient=True
            patient_pos=i
    if(is_patient==True):
        return {"name": app.patient_list[patient_pos].name, "surename": app.patient_list[patient_pos].surename}
    else:
        raise HTTPException(status_code=204, detail="Patient not found")
        return {"kek"}
 
@app.delete("/method")
def root():
    return {"method": "DELETE"}

@app.post("/patient")
async def create_item(item: Item):
    app.counter+=1
    patient = Patient(item.name,item.surename,app.counter)
    app.patient_list.append(patient)
    return {app.patient[app.counter-1]}

@app.put("/method")
def root():
    return {"method": "PUT"}

