from fastapi import APIRouter, HTTPException, status
from app.models.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password, create_access_token
from datetime import timedelta
from app.core.security import ACCESS_TOKEN_EXPIRE_MINUTES

from fastapi import APIRouter, Request, HTTPException, status
from app.core.rate_limit import limiter
from fastapi import APIRouter, Request


router = APIRouter()

# database in memory
fake_users_db = {}

@router.post("/register")
@limiter.limit("5/minute")
def register(request: Request,user: UserCreate):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    fake_users_db[user.email] = {
        "email": user.email,
        "password": hashed_password
    }
    return {"message": "User registered successfully"}

@router.post("/login")
@limiter.limit("5/minute")
def login(request: Request, user: UserLogin):
    db_user = fake_users_db.get(user.email)

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}