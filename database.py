import sqlite3
import pandas as pd

DB_NAME = "hospital.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def create_patient_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        glucose REAL,
        bmi REAL,
        blood_pressure REAL,
        insulin REAL,
        diabetes_probability REAL,
        risk_level TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_patient(name, age, gender, glucose, bmi, blood_pressure, insulin, probability, risk):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients
    (name, age, gender, glucose, bmi, blood_pressure, insulin, diabetes_probability, risk_level)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, age, gender, glucose, bmi, blood_pressure, insulin, probability, risk))

    conn.commit()
    conn.close()


def get_patients():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM patients", conn)
    conn.close()
    return df