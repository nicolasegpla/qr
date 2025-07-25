from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import routes
from app.core.config import settings
from .database import Base, engine
from .models import models  # esto importa los modelos y los registra con Base
from fastapi import Request

# Importaciones de slowapi
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core.rate_limit import limiter  # ✅ importar desde el nuevo archivo
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi import _rate_limit_exceeded_handler


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

# Configurar SlowAPI middleware y handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

@app.get("/")
@limiter.limit("5/minute")  # 🔒 Límite: 5 requests por minuto por IP
def root(request: Request):
    return {"message": "QR Management API is running"}

app.include_router(routes.router, prefix="/api/v1")