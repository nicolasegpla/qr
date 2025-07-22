from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings

# Security, secret key, algorithm, and expiration time
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hashear the password before save
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# verify the password is correct
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# create access token with expiration time
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


