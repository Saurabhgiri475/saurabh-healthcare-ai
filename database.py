import sqlite3
import datetime


# create table
def create_patient_table():

    conn = sqlite3.connect("hospital.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        glucose REAL,
        bmi REAL,
        age INTEGER,
        prediction TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()


# save patient
def save_patient(name, glucose, bmi, age, prediction):

    conn = sqlite3.connect("hospital.db")
    c = conn.cursor()

    today = datetime.datetime.now()

    c.execute("""
    INSERT INTO patients(name,glucose,bmi,age,prediction,date)
    VALUES(?,?,?,?,?,?)
    """,(name,glucose,bmi,age,prediction,today))

    conn.commit()
    conn.close()


# fetch patients
def get_patients():

    conn = sqlite3.connect("hospital.db")
    c = conn.cursor()

    c.execute("SELECT * FROM patients")

    data = c.fetchall()

    conn.close()

    return data