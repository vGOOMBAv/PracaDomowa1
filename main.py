# main.py
 
from fastapi import FastAPI
from flask import request

app = FastAPI()
 
@app.get("/method")
def root():
    buff_str=request.method
    return {"method": buff_str}
 