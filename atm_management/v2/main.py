from database import SessionLocal, User

# Function: login
def login(db):
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = db.query(User).filter(User.username == username, User.password == password).first()
    if user:
        print(f"\n✅ Welcome {user.username}!\n")
        return user
    else:
        print("\n❌ Invalid credentials. Try again.\n")
        return None

# Function: check balance
def check_balance(user):
    print(f"\n💰 Your balance: ${user.balance:.2f}\n")

# Function: deposit
def deposit(user, db):
    amount = float(input("Enter deposit amount: "))
    user.balance += amount
    db.commit()
    print(f"\n✅ Deposited ${amount:.2f}. New balance: ${user.balance:.2f}\n")

# Function: withdraw
def withdraw(user, db):
    amount = float(input("Enter withdraw amount: "))
    if amount > user.balance:
        print("\n❌ Insufficient funds.\n")
    else:
        user.balance -= amount
        db.commit()
        print(f"\n✅ Withdrawn ${amount:.2f}. New balance: ${user.balance:.2f}\n")

# Function: ATM menu
def atm_menu(user, db):
    while True:
        print("=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Choose option: ")

        if choice == "1":
            check_balance(user)
        elif choice == "2":
            deposit(user, db)
        elif choice == "3":
            withdraw(user, db)
        elif choice == "4":
            print("\n👋 Logged out successfully!\n")
            break
        else:
            print("\n❌ Invalid choice.\n")

# Main function
def main():
    db = SessionLocal()

    print("=== Welcome to Python Bank ATM ===\n")

    while True:
        user = login(db)
        if user:
            atm_menu(user, db)

if __name__ == "__main__":
    main()