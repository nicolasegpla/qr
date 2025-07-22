from pydantic import BaseModel, EmailStr

# Model for user registration
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Model for user login
class UserLogin(BaseModel):
    email: EmailStr
    password: str