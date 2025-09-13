# File: main.py
import random
import string
from auth import hash_password, verify_password
from database import conn, cursor

# --- Helper functions ---
def generate_transaction_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

def create_user(username, name, password):
    hashed = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (username, name, password) VALUES (?, ?, ?)", (username, name, hashed))
        conn.commit()
        print(f"User '{username}' created successfully.")
    except Exception as e:
        print(f"Error creating user: {e}")

def get_user_by_username(username):
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = get_user_by_username(username)
    if user and verify_password(password, user[3]):
        print(f"Welcome {user[2]}!")  # Display user's name
        return user
    else:
        print("Invalid username or password.")
        return None

def check_balance(user):
    print(f"Your balance is: ${user[4]:.2f}")

def deposit_balance(user):
    amount = float(input("Enter amount to deposit: "))
    new_balance = user[4] + amount
    cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user[0]))
    conn.commit()
    txn_id = generate_transaction_id()
    cursor.execute("INSERT INTO transactions (id, user_id, type, amount) VALUES (?, ?, ?, ?)"
                   , (txn_id, user[0], 'Deposit', amount))
    conn.commit()
    print(f"Deposited ${amount:.2f}. Transaction ID: {txn_id}")

def withdraw_balance(user):
    amount = float(input("Enter amount to withdraw: "))
    if amount > user[4]:
        print("Insufficient balance.")
        return
    new_balance = user[4] - amount
    cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user[0]))
    conn.commit()
    txn_id = generate_transaction_id()
    cursor.execute("INSERT INTO transactions (id, user_id, type, amount) VALUES (?, ?, ?, ?)"
                   , (txn_id, user[0], 'Withdraw', amount))
    conn.commit()
    print(f"Withdrawn ${amount:.2f}. Transaction ID: {txn_id}")

def transfer_balance(user):
    target_username = input("Enter recipient username: ")
    target_user = get_user_by_username(target_username)
    if not target_user:
        print("Recipient user not found.")
        return
    amount = float(input("Enter amount to transfer: "))
    if amount > user[4]:
        print("Insufficient balance.")
        return
    # Update sender
    cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (user[4]-amount, user[0]))
    # Update receiver
    cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (target_user[4]+amount, target_user[0]))
    conn.commit()
    txn_id = generate_transaction_id()
    cursor.execute("INSERT INTO transactions (id, user_id, type, amount, target_user) VALUES (?, ?, ?, ?, ?)"
                   , (txn_id, user[0], 'Transfer', amount, target_username))
    conn.commit()
    print(f"Transferred ${amount:.2f} to {target_username}. Transaction ID: {txn_id}")

def mini_statement(user):
    cursor.execute("SELECT id, type, amount, target_user, date FROM transactions WHERE user_id = ? ORDER BY date DESC LIMIT 5", (user[0],))
    rows = cursor.fetchall()
    if not rows:
        print("No transactions found.")
        return
    print("Last 5 transactions:")
    for row in rows:
        print(row)

# --- Admin panel ---
def admin_panel():
    while True:
        print("\n--- Admin Panel ---")
        print("1. Create user")
        print("2. View all users")
        print("3. View all transactions")
        print("4. Logout")
        choice = input("Enter choice: ")
        if choice == '1':
            username = input("Enter username: ")
            name = input("Enter full name: ")
            password = input("Enter password: ")
            create_user(username, name, password)
        elif choice == '2':
            cursor.execute("SELECT id, username, name, balance FROM users")
            users = cursor.fetchall()
            for u in users:
                print(u)
        elif choice == '3':
            cursor.execute("SELECT * FROM transactions")
            transactions = cursor.fetchall()
            for t in transactions:
                print(t)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

# --- Main ---
def main():
    # Ensure admin exists
    if not get_user_by_username("admin"):
        create_user("admin", "Administrator", "admin123")

    while True:
        print("\n==== Welcome to Saad's Bank ATM ====")
        print("1. Login")
        print("2. Admin Panel")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            user = login()
            if user:
                while True:
                    print("\n--- User Menu ---")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer")
                    print("5. Mini Statement")
                    print("6. Logout")
                    u_choice = input("Enter choice: ")
                    if u_choice == '1':
                        check_balance(user)
                    elif u_choice == '2':
                        deposit_balance(user)
                        user = get_user_by_username(user[1])  # refresh balance
                    elif u_choice == '3':
                        withdraw_balance(user)
                        user = get_user_by_username(user[1])
                    elif u_choice == '4':
                        transfer_balance(user)
                        user = get_user_by_username(user[1])
                    elif u_choice == '5':
                        mini_statement(user)
                    elif u_choice == '6':
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '2':
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            admin = get_user_by_username(username)
            if admin and username == "admin" and verify_password(password, admin[3]):
                admin_panel()
            else:
                print("Invalid admin credentials.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()