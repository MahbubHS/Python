import sqlite3

connect = sqlite3.connect('./database.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    dob TEXT,
    username TEXT UNIQUE,
    total_student REAL DEFAULT 0
)
''')

connect.commit()

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
dob = input("Enter date of birth (DD-MM-YYYY): ")
username = input("Enter username: ")

def get_total():
    cursor.execute("SELECT total_student FROM student")
    return cursor.fetchone()

print(get_total())
total_student = get_total()
try:
    cursor.execute(
        "INSERT INTO student (first_name, last_name, dob, username, total_student) VALUES (?, ?, ?, ?, ?)",
        (first_name, last_name, dob, username, total_student+1)
    )
    connect.commit()
    total_student = get_total()
    print(f"✅ {first_name} {last_name} added.\n🧑🏻‍🎓 Total Student is {total_student}")
    
except Exception as e:
    print(e)