from passlib.context import CryptContext
from database import SessionLocal, User

# Password context using bcrypt
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# -------- PASSWORD UTILS ----------
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

# -------- LOGIN FUNCTION ----------
def login(db):
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = db.query(User).filter(User.username == username).first()
    
    if user and verify_password(password, user.password):
        print(f"\n✅ Welcome {user.username} ({user.role})!\n")
        return user
    else:
        print("\n❌ Invalid credentials. Try again.\n")
        return None

# -------- CREATE USER (ADMIN ONLY) ----------
def create_user(db):
    username = input("New username: ")
    password = input("New password: ")
    balance = float(input("Initial balance: "))
    role = "user"

    if db.query(User).filter(User.username == username).first():
        print("❌ User already exists!\n")
        return
    
    hashed_pw = hash_password(password)
    new_user = User(username=username, password=hashed_pw, balance=balance, role=role)
    db.add(new_user)
    db.commit()
    print(f"✅ User '{username}' created successfully!\n")

# -------- CREATE DEFAULT ADMIN ON FIRST RUN ----------
def create_default_admin(db):
    admin = db.query(User).filter(User.role=="admin").first()
    if not admin:
        default_admin = User(
            username="admin",
            password=hash_password("admin123"),
            balance=0.0,
            role="admin"
        )
        db.add(default_admin)
        db.commit()
        print("✅ Default admin created!")