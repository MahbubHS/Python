from passlib.context import CryptContext
from datetime import datetime, timedelta

SECRET_KEY = "saad_secret_key_123"   # 🔑 change in production
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
