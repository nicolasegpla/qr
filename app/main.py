from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import routes
from app.core.config import settings
from .database import Base, engine
from .models import models  # esto importa los modelos y los registra con Base

app = FastAPI(title=settings.PROJECT_NAME)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# configure CORS
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "QR Management API is running"}

app.include_router(routes.router, prefix="/api/v1")