# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from datetime import timedelta

from database import SessionLocal, User, Transaction
from schemas import UserCreate, UserResponse, TransactionResponse
from auth import hash_password, verify_password, create_access_token, decode_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

app = FastAPI(title="Python Bank API", version="2.0-secure")

# OAuth2 scheme: clients send Authorization: Bearer <token>
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---- Auth Helpers ----

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    payload = decode_access_token(token)
    username: str = payload.get("sub") if payload else None
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user

# ---- Public Endpoints ----

@app.post("/register", response_model=UserResponse, summary="Create a new account")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    db_user = User(username=user.username, password=hash_password(user.password), balance=0.0)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# OAuth2PasswordRequestForm expects x-www-form-urlencoded: username, password
@app.post("/login", summary="Get JWT access token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username}, ACCESS_TOKEN_EXPIRE_MINUTES)
    return {"access_token": token, "token_type": "bearer", "expires_in_minutes": ACCESS_TOKEN_EXPIRE_MINUTES}

# ---- Authenticated (Me) Endpoints ----
# These all require Authorization: Bearer <token>

@app.get("/me", response_model=UserResponse, summary="My profile")
def me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/me/balance", summary="Check my balance")
def check_balance(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "balance": current_user.balance}

@app.post("/me/deposit", summary="Deposit money into my account")
def deposit(amount: float, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    current_user.balance += amount
    db.add(Transaction(user_id=current_user.id, type="deposit", amount=amount))
    db.commit()
    return {"message": f"Deposited {amount}", "balance": current_user.balance}

@app.post("/me/withdraw", summary="Withdraw money from my account")
def withdraw(amount: float, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    if current_user.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")
    current_user.balance -= amount
    db.add(Transaction(user_id=current_user.id, type="withdraw", amount=amount))
    db.commit()
    return {"message": f"Withdrew {amount}", "balance": current_user.balance}

@app.post("/me/transfer", summary="Transfer money to another user by username")
def transfer(receiver_username: str, amount: float, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    receiver = db.query(User).filter(User.username == receiver_username).first()
    if not receiver:
        raise HTTPException(status_code=404, detail="Receiver not found")
    if current_user.id == receiver.id:
        raise HTTPException(status_code=400, detail="Cannot transfer to self")
    if current_user.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    current_user.balance -= amount
    receiver.balance += amount
    db.add(Transaction(user_id=current_user.id, type="transfer", amount=amount))
    db.add(Transaction(user_id=receiver.id, type="receive", amount=amount))
    db.commit()
    return {"message": f"Transferred {amount} to {receiver.username}", "balance": current_user.balance}

@app.get("/me/transactions", response_model=List[TransactionResponse], summary="My transaction history")
def my_transactions(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Order latest first
    txns = db.query(Transaction).filter(Transaction.user_id == current_user.id).order_by(Transaction.timestamp.desc()).all()
    return txns