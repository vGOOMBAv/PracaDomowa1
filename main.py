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
a=0
app.counter=0
patient_list=[Patient('k','w',0),Patient('r','w',1),Patient('r','r',2)]

@app.get("/")
def root():
    return {"message": "Hello World"}
 
@app.get("/patient/{id}")
def return_patient_data(id):
    global patient_list
    is_patient=False
    patient_pos=0
    i=0
    for patient in patient_list:
        if(patient.id==id):
            is_patient=True
            patient_pos=0
        i+=1
    if(is_patient==False):
        return {"name": patient_list[patient_pos].name, "surename": patient_list[patient_pos].surename}
    else:
        raise HTTPException(status_code=204, detail="Patient not found")
        return {"kek"}
 
@app.delete("/method")
def root():
    return {"method": "DELETE"}

@app.post("/patient")
async def create_item(item: Item):
    #global patient_list
    global a
    #patient = Patient(item.name,item.surename,app.counter)
    #app.patient_list.append(patient)
    a+=1
    return {"id":a,"patient":{"name":item.name,"surename":item.surename}}

@app.put("/method")
def root():
    return {"method": "PUT"}

