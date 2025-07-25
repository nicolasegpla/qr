# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL para base de datos SQLite (local)
DATABASE_URL = "sqlite:///./qr_app.db"

# Crear el motor de conexión
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para todos los modelos
Base = declarative_base()
