from database import SessionLocal, Transaction, User
from auth import login, create_user, create_default_admin
import uuid

# ---------- TRANSACTIONS ----------
def deposit(db, user):
    amount = float(input("Enter amount to deposit: $"))
    user.balance += amount
    txn = Transaction(user_id=user.id, type="Deposit", amount=amount, txn_id=str(uuid.uuid4()))
    db.add(txn)
    db.commit()
    print(f"✅ Deposited ${amount}. New Balance is ${user.balance}\n")

def withdraw(db, user):
    amount = float(input("Enter amount to withdraw: $"))
    if amount > user.balance:
        print("❌ Insufficient balance!\n")
        return
    user.balance -= amount
    txn = Transaction(user_id=user.id, type="Withdraw", amount=amount, txn_id=str(uuid.uuid4()))
    db.add(txn)
    db.commit()
    print(f"✅ Withdrawn ${amount}. New Balance is ${user.balance}\n")

def transfer(db, user):
    target_username = input("Enter target username: ")
    amount = float(input("Enter amount to transfer: $"))
    target = db.query(User).filter_by(username=target_username).first()

    if not target:
        print("❌ Target user not found!\n")
        return
    if amount > user.balance:
        print("❌ Insufficient balance!\n")
        return
    
    user.balance -= amount
    target.balance += amount

    txn1 = Transaction(user_id=user.id, type="Transfer-Out", amount=amount, txn_id=str(uuid.uuid4()))
    txn2 = Transaction(user_id=target.id, type="Transfer-In", amount=amount, txn_id=txn1.txn_id)
    db.add_all([txn1, txn2])
    db.commit()
    print(f"✅ Transferred ${amount} to {target.username}. New Balance is ${user.balance}\n")

def mini_statement(db, user):
    txns = db.query(Transaction).filter(Transaction.user_id == user.id).order_by(Transaction.id.desc()).limit(5).all()
    print("\n📜 Mini Statement (last 5 transactions):")
    for t in txns:
        print(f"ID: {t.txn_id} | {t.type} | Amount: ${t.amount}")
    print()

# ---------- MAIN ----------
def main():
    db = SessionLocal()
    print("==== Welcome to Saad's Bank ATM ====\n")

    # Create default admin if first run
    create_default_admin(db)

    user = None
    while not user:
        user = login(db)

    if user.role == "admin":
        while True:
            print("1. Create User\n2. Logout")
            choice = input("Choose option: ")
            if choice == "1":
                create_user(db)
            elif choice == "2":
                print("👋 Logged out.\n")
                break
            else:
                print("❌ Invalid choice.\n")

    else:
        while True:
            print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Mini Statement\n6. Logout")
            choice = input("Choose option: ")
            if choice == "1":
                print(f"💰 Your balance is ${user.balance}\n")
            elif choice == "2":
                deposit(db, user)
            elif choice == "3":
                withdraw(db, user)
            elif choice == "4":
                transfer(db, user)
            elif choice == "5":
                mini_statement(db, user)
            elif choice == "6":
                print("👋 Logged out.\n")
                break
            else:
                print("❌ Invalid choice.\n")

if __name__ == "__main__":
    main()