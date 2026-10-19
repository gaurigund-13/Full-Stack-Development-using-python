# Q1. Student Feedback Form
# Create a Flask application connected to database.
# Requirements:
# ● Accept: 
# o Student Name 
# o Subject 
# o Feedback 
# ● Validate that feedback cannot be empty. 
# ● Store the feedback in the database. 
# ● Display all submitted feedback records.


from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

# Connect to database
def db_connect():
    return psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )

# Create Feedback table
def create_table():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Feedback (
            Feedback_ID SERIAL PRIMARY KEY,
            Student_Name VARCHAR(100),
            Subject VARCHAR(100),
            Feedback TEXT
        )
    """)

    con.commit()
    cur.close()
    con.close()

# Student feedback
@app.route("/", methods=["GET", "POST"])
def feedback():
    msg = ""

    if request.method == "POST":
        name = request.form["Student_Name"].strip()
        subject = request.form["Subject"].strip()
        feedback = request.form["Feedback"].strip()

        if feedback == "":
            msg = "Feedback cannot be empty."

        else:
            con = db_connect()
            cur = con.cursor()

            cur.execute(
                """INSERT INTO Feedback
                (Student_Name, Subject, Feedback)
                VALUES (%s, %s, %s)""",
                (name, subject, feedback)
            )

            con.commit()
            cur.close()
            con.close()

            msg = "Feedback submitted successfully!"

    # Display all feedback records
    con = db_connect()
    cur = con.cursor()

    cur.execute("SELECT * FROM Feedback ORDER BY Feedback_ID")
    records = cur.fetchall()

    cur.close()
    con.close()

    return render_template("index.html", msg=msg, records=records)


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
