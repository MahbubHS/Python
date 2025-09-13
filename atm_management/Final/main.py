# bank_app.py
import sqlite3
import random
import string
from passlib.context import CryptContext

# ---------------- PASSLIB CONTEXT ----------------
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

# ---------------- DATABASE ----------------
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    name TEXT,
    balance REAL DEFAULT 0
)
""")

# Transactions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id TEXT PRIMARY KEY,
    user_id INTEGER,
    type TEXT,
    amount REAL,
    target_user TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# ---------------- TRANSACTION ID ----------------
def generate_txn_id(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

# ---------------- USER FUNCTIONS ----------------
def create_user():
    username = input("Enter new username: ")
    password = input("Enter password: ")
    name = input("Enter full name: ")
    hashed = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (username, password, name) VALUES (?, ?, ?)",
                       (username, hashed, name))
        conn.commit()
        print(f"✅ User {username} created successfully!")
    except sqlite3.IntegrityError:
        print("❌ Username already exists!")

def login():
    username = input("Username: ")
    password = input("Password: ")
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    if user and verify_password(password, user[2]):
        print(f"\nWelcome {user[3]} to Saad's Bank ATM! 💰")
        if username == "admin":
            admin_panel()
        else:
            user_panel(user)
    else:
        print("❌ Invalid username or password!")

def user_panel(user):
    while True:
        print("\nUser Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Mini Statement")
        print("6. Logout")
        choice = input("Choose: ")

        if choice == "1":
            print(f"💰 Current Balance: ${user[4]:.2f}")

        elif choice == "2":
            deposit(user)

        elif choice == "3":
            withdraw(user)

        elif choice == "4":
            transfer(user)

        elif choice == "5":
            mini_statement(user)

        elif choice == "6":
            break

        else:
            print("❌ Invalid option!")

# ---------------- TRANSACTION FUNCTIONS ----------------
def deposit(user):
    amount = float(input("Enter amount to deposit: "))
    new_balance = user[4] + amount
    cursor.execute("UPDATE users SET balance=? WHERE id=?", (new_balance, user[0]))
    txn_id = generate_txn_id()
    cursor.execute("INSERT INTO transactions (id, user_id, type, amount) VALUES (?, ?, ?, ?)",
                   (txn_id, user[0], "Deposit", amount))
    conn.commit()
    user = list(user)
    user[4] = new_balance
    print(f"✅ Deposited ${amount:.2f}. Transaction ID: {txn_id}")

def withdraw(user):
    amount = float(input("Enter amount to withdraw: "))
    if amount > user[4]:
        print("❌ Insufficient balance!")
        return
    new_balance = user[4] - amount
    cursor.execute("UPDATE users SET balance=? WHERE id=?", (new_balance, user[0]))
    txn_id = generate_txn_id()
    cursor.execute("INSERT INTO transactions (id, user_id, type, amount) VALUES (?, ?, ?, ?)",
                   (txn_id, user[0], "Withdraw", amount))
    conn.commit()
    user = list(user)
    user[4] = new_balance
    print(f"✅ Withdrawn ${amount:.2f}. Transaction ID: {txn_id}")

def transfer(user):
    target_username = input("Enter recipient username: ")
    cursor.execute("SELECT * FROM users WHERE username=?", (target_username,))
    target_user = cursor.fetchone()
    if not target_user:
        print("❌ User not found!")
        return
    amount = float(input("Enter amount to transfer: "))
    if amount > user[4]:
        print("❌ Insufficient balance!")
        return
    # Deduct from sender
    new_balance = user[4] - amount
    cursor.execute("UPDATE users SET balance=? WHERE id=?", (new_balance, user[0]))
    # Add to recipient
    target_new_balance = target_user[4] + amount
    cursor.execute("UPDATE users SET balance=? WHERE id=?", (target_new_balance, target_user[0]))
    # Record transaction
    txn_id = generate_txn_id()
    cursor.execute("INSERT INTO transactions (id, user_id, type, amount, target_user) VALUES (?, ?, ?, ?, ?)",
                   (txn_id, user[0], "Transfer", amount, target_username))
    conn.commit()
    user = list(user)
    user[4] = new_balance
    print(f"✅ Transferred ${amount:.2f} to {target_username}. Transaction ID: {txn_id}")

def mini_statement(user):
    cursor.execute("SELECT id, type, amount, target_user, date FROM transactions WHERE user_id=? ORDER BY date DESC LIMIT 5", (user[0],))
    txns = cursor.fetchall()
    if not txns:
        print("No transactions found ❌")
        return
    print("\n=== Mini Statement (Last 5 transactions) ===")
    for t in txns:
        print(f"ID:{t[0]} | Type:{t[1]} | Amount:${t[2]:.2f} | Target:{t[3]} | Date:{t[4]}")

# ---------------- ADMIN PANEL ----------------
def admin_panel():
    while True:
        print("\nAdmin Panel:")
        print("1. Create User")
        print("2. View All Users")
        print("3. Delete User")
        print("4. View User Transactions")
        print("5. Logout")
        choice = input("Choose: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            cursor.execute("SELECT id, username, name, balance FROM users WHERE username!='admin'")
            users = cursor.fetchall()
            if users:
                print("=== All Users ===")
                for u in users:
                    print(f"ID:{u[0]} | Username:{u[1]} | Name:{u[2]} | Balance:${u[3]:.2f}")
            else:
                print("No users found ❌")
        elif choice == "3":
            del_username = input("Enter username to delete: ")
            if del_username == "admin":
                print("❌ Cannot delete admin!")
                continue
            cursor.execute("SELECT * FROM users WHERE username=?", (del_username,))
            if cursor.fetchone():
                cursor.execute("DELETE FROM users WHERE username=?", (del_username,))
                conn.commit()
                print(f"✅ User {del_username} deleted!")
            else:
                print("❌ User not found!")
        elif choice == "4":
            username = input("Enter username to view transactions: ")
            cursor.execute("SELECT id FROM users WHERE username=?", (username,))
            user_row = cursor.fetchone()
            if not user_row:
                print("❌ User not found!")
                continue
            user_id = user_row[0]
            cursor.execute("SELECT id, type, amount, target_user, date FROM transactions WHERE user_id=?", (user_id,))
            txns = cursor.fetchall()
            if txns:
                print(f"=== Transactions for {username} ===")
                for t in txns:
                    print(f"ID:{t[0]} | Type:{t[1]} | Amount:${t[2]:.2f} | Target:{t[3]} | Date:{t[4]}")
            else:
                print("No transactions found ❌")
        elif choice == "5":
            break
        else:
            print("❌ Invalid option!")

# ---------------- DEFAULT ADMIN ----------------
def create_default_admin():
    cursor.execute("SELECT * FROM users WHERE username='admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, password, name) VALUES (?, ?, ?)",
                       ("admin", hash_password("admin123"), "Bank Admin"))
        conn.commit()

# ---------------- MAIN ----------------
def main():
    create_default_admin()
    while True:
        print("\n==== Welcome to Saad's Bank ATM ====")
        print("1. Login")
        print("2. Exit")
        choice = input("Choose: ")

        if choice == "1":
            login()
        elif choice == "2":
            print("Thank you for using Saad's Bank ATM! 👋")
            break
        else:
            print("❌ Invalid option!")

if __name__ == "__main__":
    main()