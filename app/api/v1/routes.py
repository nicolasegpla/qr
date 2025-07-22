from fastapi import APIRouter
from app.api.v1 import auth


router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])