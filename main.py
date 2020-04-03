# main.py
 
from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic"}
 
@app.get("/{method}")
async def read_item(method: str):
    buffStr=method.upper()
    return {"method": buffStr}   