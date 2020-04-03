# main.py
 
from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def root():
    return {"message": "Hello World"}
 
@app.get("/{method}")
async def read_item(method: str):
    return {"method": f"{method}"}