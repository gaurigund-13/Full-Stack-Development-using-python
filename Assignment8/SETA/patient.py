#  Create a Flask application connected with PostgreSQL. Create a Patient table and Search 
# a patient using Patient ID and display the details.

from flask import Flask, request
import psycopg2

app = Flask(__name__)

# Database Connection
def db_connect():
    return psycopg2.connect(
        dbname = 'hospital',
        user = 'postgres',
        password = "root",
        host = "localhost",
        port = "5432"
    )

# create patient table
@app.route('/create_table')
def create_table():
    try:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Patient(
              patient_id SERIAL PRIMARY KEY,
              name VARCHAR(100),
              age INT,
              disease VARCHAR(100)
            );
        
        """)

        conn.commit()
        cur.close()
        conn.close()
        return "Patient Table Created Successfully!"

    except Exception as e:
        return f"Error : {e}"

# insert records in patient table
@app.route('/insert_records')
def insert_patients():
    try:
        conn = db_connect()
        cur = conn.cursor()
        patients = [
            ("Rahul", 24, "Fever"),
            ("Priya", 31, "Diabetes"),
            ("Amit", 45, "Hypertension"),
            ("Sneha", 28, "Asthma"),
            ("Vikram", 52, "Arthritis")
        ]

        cur.executemany("INSERT INTO Patient(name,age,disease) VALUES(%s,%s,%s)",patients)
        conn.commit()
        cur.close()
        conn.close()

        return "5 record inserted sucessfully!"

    except Exception as e:
        return f"Error: {e}"

# Search patient by ID
@app.route('/search_patient/<int:pid>')
def search_patient(pid):
    try:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Patient WHERE patient_id = %s;",(pid,))
        patient = cur.fetchone()

        cur.close()
        conn.close()

        if patient:
            return f"Patient Details : ID={patient[0]}, Name={patient[1]}, Age={patient[2]}, Disease={patient[3]}"
        else:
            return "No patient associated with that ID"

    except Exception as e:
        return f"Error : {e}"
if __name__ == '__main__':
    app.run(debug=True)