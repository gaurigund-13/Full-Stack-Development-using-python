from flask import Flask
import psycopg2

app = Flask(__name__)

# Connection route
@app.route('/connect')
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="student",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        conn.close()
        return "Database Connected Successfully"
    except Exception as e:
        return f"Error: {e}"

# Table creation 
@app.route('/create_table')
def create_table():
    try:
        conn = psycopg2.connect(
            dbname="student",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Student (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                course VARCHAR(50)
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        return "Student Table Created Successfully"
    except Exception as e:
        return f"Error: {e}"

# Insert records 
@app.route('/insert')
def insert_students():
    try:
        conn = psycopg2.connect(
            dbname="student",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        students = [
            ('Rahul', 24, 'Computer Science'),
            ('Gauri', 22, 'Information Technology'),
            ('Siya', 20, 'Data Science'),
            ('Riya', 23, 'Cyber Security'),
            ('Diya', 21, 'Artificial Intelligence')
        ]
        cur.executemany("INSERT INTO Student (name, age, course) VALUES (%s, %s, %s);", students)
        conn.commit()
        cur.close()
        conn.close()
        return "5 Student Records Inserted Successfully"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
