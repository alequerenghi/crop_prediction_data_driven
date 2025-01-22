import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    salt TEXT NOT NULL
    )
""")
print("Created 'users' table (if it didn't already exist)")
try:
    cursor.execute("INSERT INTO users (username, hashed_password, salt) VALUES (?, ?, ?)", ("admin", "admin", "1234"))
    conn.commit()
    print("test user 'admin' added")
except sqlite3.IntegrityError:
    print("'admin' user already exist")

cursor.execute("SELECT username, hashed_password, salt FROM users")
users = cursor.fetchall()

if users:
    print("\nUsers in database:")
    for user in users:
        print(f"Username: {user[0]}, Password: {user[1]}, Salt: {user[2]}")
else:
    print("No results founded in database.")

conn.close()
print("\nDatabase connection closed")
