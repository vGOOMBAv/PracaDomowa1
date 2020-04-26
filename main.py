# main.py

from hashlib import sha256
from starlette.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, Response, HTTPException, FastAPI
import secrets


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

security = HTTPBasic()
app.secret_key = "very constatn and random secret, best 64 characters, here it is."

session_tokens = []

@app.post("/login")
def get_current_user(response: Response, credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "trudnY")
    correct_password = secrets.compare_digest(credentials.password, "PaC13Nt")
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    session_token = sha256(bytes(f"{credentials.username}{credentials.password}{app.secret_key}", encoding='utf8')).hexdigest()
    response.set_cookie(key="session_token", value=session_token)
    session_tokens.append(session_token)
    return RedirectResponse(url='/welcome')
    


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

@app.put("/method")
def root():
    return {"method": "PUT"}

