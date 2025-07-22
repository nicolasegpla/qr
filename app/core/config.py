from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    SECRET_KEY = str(os.getenv("SECRET_KEY", "default_secret_key"))
    PROJECT_NAME: str = "QR Management API"
    API_V1_STR: str = "/api/v1"

settings = Settings()
