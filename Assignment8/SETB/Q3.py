#  Create a Flask application connected with PostgreSQL. Create a Patient table with ID, 
# Name and Age and insert 5 records.

from flask import Flask
import psycopg2

app = Flask(__name__)

def db_connect():
     conn = psycopg2.connect(
          dbname = 'hospital',
          user = 'postgres',
          password = 'root',
          host = 'localhost',
          port = '5432'    
     )

     return conn

# table creation
@app.route('/create_table')
def table_create():

    try:

        conn = db_connect()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Patient1(
                pid serial PRIMARY KEY,
                name VARCHAR(100),
                age INT
            );
        """)

        conn.commit()
        cur.close()
        conn.close()
        return "Table created sucessfully"
    
    except Exception as e:
        return f"Error :{e}"


# insert records in Patient1
@app.route('/insert_record')
def insert_record():

    try:

        conn = db_connect()
        cur = conn.cursor()

        patients = [
                    ("Aditya", 24 ),
                    ("Priya", 31 ),
                    ("Vaibhav", 22 ),
                    ("Sneha", 28 ),
                    ("Vikram", 52)
                ]

        cur.executemany("INSERT INTO Patient1(name, age) VALUES (%s,%s);",patients)

        conn.commit()
        cur.close()
        conn.close()

        return "record inserted sucessfully"

    except Exception as e:
        return f"Error :{e}"

if __name__ == '__main__':
    app.run(debug=True)