from database import SessionLocal, User

db = SessionLocal()
db.add_all([
    User(username="saad", password="1234", balance=1000),
    User(username="alice", password="pass", balance=500),
])
db.commit()