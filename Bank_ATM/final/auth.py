# auth.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password):
    """Hash a plain text password"""
    return pwd_context.hash(password)

def verify_password(password, hashed):
    """Verify a plain text password against a hashed password"""
    return pwd_context.verify(password, hashed)