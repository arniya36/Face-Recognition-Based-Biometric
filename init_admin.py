import sqlite3
from bcrypt import hashpw, gensalt
import os

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
""")

admin_username = os.getenv('USER1')
admin_password = os.getenv('PASS1') 

hashed_password = hashpw(admin_password.encode("utf-8"), gensalt())

try:
    cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)", (admin_username, hashed_password))
    print("Admin user created successfully!")
except sqlite3.IntegrityError:
    print("Admin user already exists!")

admin_username = os.getenv('USER2')
admin_password = os.getenv('PASS2')

hashed_password = hashpw(admin_password.encode("utf-8"), gensalt())

try:
    cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)", (admin_username, hashed_password))
    print("Admin user created successfully!")
except sqlite3.IntegrityError:
    print("Admin user already exists!")

admin_username = os.getenv('USER3')
admin_password = os.getenv('PASS3') 

hashed_password = hashpw(admin_password.encode("utf-8"), gensalt())

try:
    cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)", (admin_username, hashed_password))
    print("Admin user created successfully!")
except sqlite3.IntegrityError:
    print("Admin user already exists!")

admin_username = os.getenv('USER4')
admin_password = os.getenv('PASS4')

hashed_password = hashpw(admin_password.encode("utf-8"), gensalt())

try:
    cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)", (admin_username, hashed_password))
    print("Admin user created successfully!")
except sqlite3.IntegrityError:
    print("Admin user already exists!")

conn.commit()
conn.close()
