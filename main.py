from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

users = {
    "nithya": "1234",
    "admin": "admin123"
}

@app.post("/verify")
def verify(data: LoginRequest):
    if data.username in users and users[data.username] == data.password:
        return {"status": "success"}
    return {"status": "fail"}