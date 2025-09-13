# main.py
import random
import string
from auth import hash_password, verify_password
from database import conn, cursor

def generate_transaction_id(length=10):
    """Generate alphanumeric-only transaction ID"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def create_default_admin():
    """Create default admin if not exists"""
    cursor.execute("SELECT * FROM users WHERE username = ?", ("admin",))
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO users (username, name, password, is_admin) VALUES (?, ?, ?, ?)",
            ("admin", "Admin", hash_password("admin123"), 1)
        )
        conn.commit()

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user and verify_password(password, user[3]):
        print(f"\n✅ Welcome {user[2]}!\n")
        if user[5] == 1:
            admin_panel(user)
        else:
            user_panel(user)
    else:
        print("❌ Invalid username or password!")

def admin_panel(admin_user):
    while True:
        print("=== Admin Panel ===")
        print("1. Create User")
        print("2. View Users")
        print("3. View Transactions")
        print("4. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            view_users()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice!")

def create_user():
    username = input("Enter new username: ")
    name = input("Enter user's full name: ")
    balance = float(input("Enter initial balance: "))
    password = hash_password(input("Enter password for this user: "))
    try:
        cursor.execute(
            "INSERT INTO users (username, name, password, balance) VALUES (?, ?, ?, ?)",
            (username, name, password, balance)
        )
        conn.commit()
        print(f"✅ User {name} created successfully!")
    except:
        print("❌ Username already exists!")

def view_users():
    cursor.execute("SELECT id, username, name, balance FROM users")
    users = cursor.fetchall()
    for u in users:
        print(f"ID:{u[0]} | Username:{u[1]} | Name:{u[2]} | Balance:{u[3]}")

def view_transactions():
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    for t in transactions:
        print(t)

def user_panel(user):
    while True:
        print("=== User Menu ===")
        print("1. Check Balance")
        print("2. Deposit Balance")
        print("3. Withdraw Balance")
        print("4. Transfer Balance")
        print("5. Mini Statement")
        print("6. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"💰 Current Balance: {user[4]}")
        elif choice == "2":
            deposit_balance(user)
        elif choice == "3":
            withdraw_balance(user)
        elif choice == "4":
            transfer_balance(user)
        elif choice == "5":
            mini_statement(user)
        elif choice == "6":
            break
        else:
            print("❌ Invalid choice!")

def deposit_balance(user):
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        new_balance = user[4] + amount
        cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user[0]))
        cursor.execute(
            "INSERT INTO transactions (id, user_id, type, amount) VALUES (?, ?, ?, ?)",
            (generate_transaction_id(), user[0], "Deposit", amount)
        )
        conn.commit()
        user_list_index_update(user, new_balance)
        print("✅ Deposit successful!")
    else:
        print("❌ Invalid amount!")

def withdraw_balance(user):
    amount = float(input("Enter withdrawal amount: "))
    if 0 < amount <= user[4]:
        new_balance = user[4] - amount
        cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user[0]))
        cursor.execute(
            "INSERT INTO transactions (id, user_id, type, amount) VALUES (?, ?, ?, ?)",
            (generate_transaction_id(), user[0], "Withdraw", amount)
        )
        conn.commit()
        user_list_index_update(user, new_balance)
        print("✅ Withdrawal successful!")
    else:
        print("❌ Invalid amount or insufficient balance!")

def transfer_balance(user):
    target_username = input("Enter target username: ")
    cursor.execute("SELECT * FROM users WHERE username = ?", (target_username,))
    target_user = cursor.fetchone()
    if target_user:
        amount = float(input("Enter amount to transfer: "))
        if 0 < amount <= user[4]:
            # Deduct from sender
            new_balance_sender = user[4] - amount
            cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance_sender, user[0]))
            # Add to receiver
            new_balance_target = target_user[4] + amount
            cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance_target, target_user[0]))
            # Transaction entry
            cursor.execute(
                "INSERT INTO transactions (id, user_id, type, amount, target_user) VALUES (?, ?, ?, ?, ?)",
                (generate_transaction_id(), user[0], "Transfer", amount, target_username)
            )
            conn.commit()
            user_list_index_update(user, new_balance_sender)
            print("✅ Transfer successful!")
        else:
            print("❌ Invalid amount or insufficient balance!")
    else:
        print("❌ Target user not found!")

def mini_statement(user):
    cursor.execute("SELECT * FROM transactions WHERE user_id = ? ORDER BY date DESC LIMIT 5", (user[0],))
    transactions = cursor.fetchall()
    for t in transactions:
        print(t)

def user_list_index_update(user, new_balance):
    """Update user tuple balance locally for the session"""
    user_list = list(user)
    user_list[4] = new_balance
    return tuple(user_list)

if __name__ == "__main__":
    create_default_admin()
    while True:
        print("\n==== Welcome to Saad's Bank ATM ====")
        login()