# main.py
 
from fastapi import FastAPI
from pydantic import BaseModel
from flask import Flask

class Item(BaseModel):
	name:str
	surename:str

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
 
@app.get("/method")
def root():
    return {"method": "GET"}
 
@app.delete("/method")
def root():
    return {"method": "DELETE"}

@app.post("/patient")
async def create_item(item: Item):
    #b_name=item.name.upper()
    #b_surname=item.surename.upper()
    #return {"id":a,"patient":{"name":item.name,"surename":item.surename}
    a=a+1
    return {"id":a,"patient":{"name":item.name,"surename":item.surename}}

@app.put("/method")
def root():
    return {"method": "PUT"}

@app.context_processor
def context_processpr():
    return dict(a=0)