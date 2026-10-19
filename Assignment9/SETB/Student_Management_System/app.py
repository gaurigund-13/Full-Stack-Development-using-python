# Q1. Student Management System with Update Operation
# Create a Flask application connected to database.
# Requirements:
# ● Create Student table. 
# ● Insert and display student records. 
# ● Update the course of a student using Student_ID. 
# ● Display updated records.

from flask import Flask , request, render_template, redirect
import psycopg2

app = Flask(__name__)

# Conncet to postgres
def db_conncet():
    return psycopg2.connect(
        dbname = 'studentdb',
        user = 'postgres',
        password = 'root',
        host = 'localhost',
        port = '5432'
    )

# Create table Student
def create_table():
    con = db_conncet()
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

# Add students
@app.route('/', methods= ['GET','POST'])
def add_student():

    con = db_conncet()
    cur = con.cursor()

    if request.method == 'POST':

        Name = request.form.get('Name')
        Course = request.form.get('Course')

        cur.execute(
            "INSERT INTO Student(Name, Course) VALUES(%s,%s)",(Name, Course)
        )

        con.commit()

        cur.close()
        con.close()

        return redirect('/')

    return render_template('add.html')

# Update student course
@app.route('/update', methods = ['GET','POST'])
def update():

    con = db_conncet()
    cur = con.cursor()

    if request.method == "POST":

        Student_ID = request.form.get("Student_ID")
        Course = request.form.get("New_Course")

        cur.execute(
            "UPDATE Student SET Course = %s WHERE Student_ID = %s",
            (Course, Student_ID)
        )

        con.commit()

    cur.execute("SELECT * FROM Student ORDER BY Student_ID")
    students = cur.fetchall()

    cur.close()
    con.close()

    return render_template('update.html', students=students)

if __name__ == '__main__':
    create_table()
    app.run(debug = True)





