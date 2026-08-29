import sqlite3
import bcrypt

def init_db():
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS password_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def is_reused_password(user_id: str, new_password: str) -> bool:
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM password_history WHERE user_id = ?", (user_id,))
    records = cursor.fetchall()
    conn.close()

    for (stored_hash,) in records:
        if bcrypt.checkpw(new_password.encode("utf-8"), stored_hash.encode("utf-8")):
            return True
    return False

def save_password_hash(user_id: str, password: str):
    salt = bcrypt.gensalt()
    pw_hash = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")
    
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO password_history (user_id, password_hash) VALUES (?, ?)", (user_id, pw_hash))
    conn.commit()
    conn.close()