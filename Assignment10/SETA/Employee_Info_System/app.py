# Q2. Employee Information Form
# Create a Flask application connected to database.
# Requirements:
# ● Accept: 
# o Employee ID 
# o Employee Name 
# o Department 
# ● Validate that all fields are compulsory. 
# ● Store data in the database. 
# ● Display entered information after successful submission.

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

# Create Employee table
def create_table():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Employee1 (
            Employee_ID INT PRIMARY KEY,
            Name VARCHAR(100),
            Department VARCHAR(100)
        )
    """)

    con.commit()
    cur.close()
    con.close()

# Employee information
@app.route("/", methods=["GET", "POST"])
def employee():
    msg = ""
    emp = None

    if request.method == "POST":
        eid = request.form["Employee_ID"].strip()
        name = request.form["Name"].strip()
        department = request.form["Department"].strip()

        if eid == "" or name == "" or department == "":
            msg = "Please fill in all fields."

        else:
            con = db_connect()
            cur = con.cursor()

            cur.execute(
                """INSERT INTO Employee1
                (Employee_ID, Name, Department)
                VALUES (%s, %s, %s)""",
                (eid, name, department)
            )

            con.commit()

            emp = (eid, name, department)
            msg = "Employee information saved successfully!"

            cur.close()
            con.close()

    return render_template("index.html", msg=msg, emp=emp)


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
