# main.py
 
from hashlib import sha256
from fastapi import FastAPI, Response, Cookie, HTTPException
from pydantic import BaseModel
from requests.auth import HTTPBasicAuth

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
a=-1

patient_list=[]


@app.post("/login/")
def create_cookie(auth):
    auth_check=HTTPBasicAuth('trudnY', 'PaC13Nt')
    if auth==auth_check:
        URL="http://testserver-python-level-up.herokuapp.com/welcome"
        app.get(URL)
    else:
        raise HTTPException(status_code=301)
    


@app.get("/")
def root():
    app.get('/welcome')
    

@app.get("/welcome")
def root():
    return {"message": "Hello World welcome"}
 
@app.get("/patient/{id}")
def return_patient_data(id):
    global patient_list
    is_patient=False
    patient_pos=0
    
    if(int(id)<=a):
        is_patient=True
    
    if(is_patient==True):
        return {"name": patient_list[int(id)].name, "surename": patient_list[int(id)].surename}
    else:
        raise HTTPException(status_code=204, detail="Patient not found")
        return {"kek"}
 
@app.delete("/method")
def root():
    return {"method": "DELETE"}

@app.post("/patient")
async def create_item(item: Item):
    global patient_list
    global a
    patient_list.append(Patient(item.name,item.surename,a))
    a+=1
    return {"id":a,"patient":{"name":item.name,"surename":item.surename}}

@app.put("/method")
def root():
    return {"method": "PUT"}

