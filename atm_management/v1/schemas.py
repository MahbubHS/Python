from pydantic import BaseModel
from typing import List
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    balance: float

    class Config:
        orm_mode = True

class TransactionResponse(BaseModel):
    id: int
    type: str
    amount: float
    timestamp: datetime

    class Config:
        orm_mode = True