# Q1. Student Management System
# Create a Flask application connected to database.
# Requirements:
# ● Create a table Student (Student_ID, Name, Course). 
# ● Insert at least 3 student records using an HTML form. 
# ● Display all student records on a web page.

from flask import Flask , request, render_template
import psycopg2

app = Flask(__name__)

# Conncet to database
def get_connect():
    conn = psycopg2.connect(
       dbname = 'studentdb',
       user = 'postgres',
       password = 'root',
       host = 'localhost',
       port = '5432'
    )

    return conn

def create_table():
    con = get_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            Student_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Course VARCHAR(100)
        );
    """)

    con.commit()
    cur.close()
    con.close()

   

@app.route('/student', methods=['GET','POST'])
def student():

    con = get_connect()
    cur = con.cursor()

    if request.method == 'POST':

        Name = request.form.get("Name")
        Course = request.form.get("Course")

        cur.execute(
            "INSERT INTO Student( Name,Course) VALUES(%s,%s)",
            ( Name, Course)
        )

        con.commit()

    cur.execute("SELECT * FROM Student ORDER BY Student_ID")
    students = cur.fetchall()

    cur.close()
    con.close()

    return render_template("index.html", students=students)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)