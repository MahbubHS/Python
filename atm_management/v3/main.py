from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, User, Transaction, engine
from schemas import UserCreate, UserLogin, UserResponse, TransactionResponse
from auth import hash_password, verify_password
from datetime import timedelta
from typing import List

app = FastAPI()

# Dependency: DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🟢 Register
@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(username=user.username, password=hash_password(user.password), balance=0.0)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 🟢 Login
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"sub": db_user.username}

# 🟢 Check Balance
@app.get("/balance/{username}")
def check_balance(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": user.username, "balance": user.balance}

# 🟢 Deposit
@app.post("/deposit/{username}")
def deposit(username: str, amount: float, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.balance += amount
    db.add(Transaction(user_id=user.id, type="deposit", amount=amount))
    db.commit()
    return {"message": f"Deposited {amount}", "balance": user.balance}

# 🟢 Withdraw
@app.post("/withdraw/{username}")
def withdraw(username: str, amount: float, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")
    user.balance -= amount
    db.add(Transaction(user_id=user.id, type="withdraw", amount=amount))
    db.commit()
    return {"message": f"Withdrew {amount}", "balance": user.balance}

# 🟢 Transfer Money
@app.post("/transfer")
def transfer(sender: str, receiver: str, amount: float, db: Session = Depends(get_db)):
    sender_user = db.query(User).filter(User.username == sender).first()
    receiver_user = db.query(User).filter(User.username == receiver).first()

    if not sender_user or not receiver_user:
        raise HTTPException(status_code=404, detail="User not found")
    if sender_user.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    sender_user.balance -= amount
    receiver_user.balance += amount
    db.add(Transaction(user_id=sender_user.id, type="transfer", amount=amount))
    db.add(Transaction(user_id=receiver_user.id, type="receive", amount=amount))
    db.commit()
    return {"message": f"Transferred {amount} from {sender} to {receiver}"}

# 🟢 Transaction History
@app.get("/transactions/{username}", response_model=List[TransactionResponse])
def transactions(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.transactions