import sqlite3
import hashlib


def create_users_table():

    conn = sqlite3.connect("hospital.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT,
        role TEXT
    )
    """)

    conn.commit()
    conn.close()


def create_default_admin():

    conn = sqlite3.connect("hospital.db")
    c = conn.cursor()

    password = hashlib.sha256("admin123".encode()).hexdigest()

    c.execute("SELECT * FROM users WHERE username='admin'")

    if c.fetchone() is None:

        c.execute(
        "INSERT INTO users VALUES(?,?,?)",
        ("admin",password,"admin")
        )

    conn.commit()
    conn.close()


def login(username,password):

    conn = sqlite3.connect("hospital.db")
    c = conn.cursor()

    password = hashlib.sha256(password.encode()).hexdigest()

    c.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username,password)
    )

    result = c.fetchone()

    conn.close()

    return result