# database.py
import sqlite3
#import os

# Custom folder for the database
#db_folder = '/storage/emulated/0/documents/Python/Bank_ATM/final/Database/'
#os.makedirs(db_folder, exist_ok=True)
#db_path = os.path.join(db_folder, 'bank.db')

# Connect to SQLite database
conn = sqlite3.connect('./bank.db')
cursor = conn.cursor()

# Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    name TEXT,
    password TEXT,
    balance REAL DEFAULT 0,
    is_admin INTEGER DEFAULT 0
)
''')

# Transactions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id TEXT PRIMARY KEY,
    user_id INTEGER,
    type TEXT,
    amount REAL,
    target_user TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()