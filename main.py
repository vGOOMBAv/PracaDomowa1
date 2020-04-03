# main.py
 
from fastapi import FastAPI
from flask import request

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

@app.post("/method")
def root():
    return {"method": "POST"}

@app.put("/method")
def root():
    return {"method": "PUT"}
 