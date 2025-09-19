from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name : str = "Fast App"
    admin_email : str = "admin@example.com"

def get_settings():
    return Settings()

@app.post("/signup")
def signup(user: UserSignup):
    return {"Message": f'User {user.username} signed up successfully!', "User": user}

@app.get('/settings')
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings