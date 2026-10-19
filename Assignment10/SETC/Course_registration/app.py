
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

# Create Registration table
def create_table():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Registration (
            Registration_ID SERIAL PRIMARY KEY,
            Student_Name VARCHAR(100),
            Email VARCHAR(100),
            Course_Name VARCHAR(100)
        )
    """)

    con.commit()
    cur.close()
    con.close()

# Course registration
@app.route("/", methods=["GET", "POST"])
def register():
    msg = ""

    if request.method == "POST":
        name = request.form["Student_Name"].strip()
        email = request.form["Email"].strip()
        course = request.form["Course_Name"].strip()

        if name == "" or email == "" or course == "":
            msg = "Please fill in all fields."

        elif "@" not in email:
            msg = "Email must contain '@'."

        else:
            con = db_connect()
            cur = con.cursor()

            cur.execute(
                """INSERT INTO Registration
                (Student_Name, Email, Course_Name)
                VALUES (%s, %s, %s)""",
                (name, email, course)
            )

            con.commit()
            cur.close()
            con.close()

            msg = "Course registered successfully!"

    # Display all registered students
    con = db_connect()
    cur = con.cursor()

    cur.execute("SELECT * FROM Registration ORDER BY Registration_ID")
    students = cur.fetchall()

    cur.close()
    con.close()

    return render_template("index.html", msg=msg, students=students)


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
