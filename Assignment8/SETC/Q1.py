# Create a Flask application connected with PostgreSQL. Insert 5 employee records. 
# Update an employee's salary and delete an employee using Employee ID. Display the final 
# employee records.

from flask import Flask
import psycopg2

app = Flask(__name__)

# Database connection
def db_connect():
    return psycopg2.connect(
        dbname="employee",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )

# Insert 5 employee records
@app.route('/insert')
def insert_records():
    try:
        conn = db_connect()
        cur = conn.cursor()

        # Create Employee table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Employee1 (
                emp_id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                department VARCHAR(100),
                salary FLOAT
            );
        """)

        # Insert records only if table is empty
        cur.execute("SELECT COUNT(*) FROM Employee1")
        count = cur.fetchone()[0]

        if count == 0:
            employees = [
                ("Rahul Sharma", "IT", 45000),
                ("Priya Patil", "HR", 40000),
                ("Amit Shrivastav", "Finance", 50000),
                ("Sneha Roy", "Marketing", 42000),
                ("Vikram Varma", "IT", 55000)
            ]

            cur.executemany("""
                INSERT INTO Employee1 (name, department, salary)
                VALUES (%s, %s, %s)
            """, employees)

            conn.commit()
            message = "5 Employee Records Inserted Successfully!"
        else:
            message = "Employee records already exist."

        cur.close()
        conn.close()

        return message

    except Exception as e:
        return f"Error: {e}"


# Update employee salary using Employee ID
@app.route('/update/<int:eid>')
def update_salary(eid):
    try:
        conn = db_connect()
        cur = conn.cursor()

        new_salary = 60000

        cur.execute("""
            UPDATE Employee1
            SET salary = %s
            WHERE emp_id = %s
            RETURNING emp_id, name, salary
        """, (new_salary, eid))

        employee = cur.fetchone()
        conn.commit()

        cur.close()
        conn.close()

        if employee:
            return (
                f"Salary Updated Successfully!<br>"
                f"Employee ID: {employee[0]}<br>"
                f"Name: {employee[1]}<br>"
                f"New Salary: ₹{employee[2]:.2f}"
            )
        else:
            return "Employee Not Found!"

    except Exception as e:
        return f"Error: {e}"


# Delete employee using Employee ID
@app.route('/delete/<int:eid>')
def delete_employee(eid):
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM Employee1
            WHERE emp_id = %s
            RETURNING emp_id, name
        """, (eid,))

        employee = cur.fetchone()
        conn.commit()

        cur.close()
        conn.close()

        if employee:
            return (
                f"Employee Deleted Successfully!<br>"
                f"Employee ID: {employee[0]}<br>"
                f"Name: {employee[1]}"
            )
        else:
            return "Employee Not Found!"

    except Exception as e:
        return f"Error: {e}"


# Display final employee records
@app.route('/display')
def display_records():
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT emp_id, name, department, salary
            FROM Employee1
            ORDER BY emp_id
        """)

        employees = cur.fetchall()

        cur.close()
        conn.close()

        if not employees:
            return "No Employee Records Found!"

        output = "<h2>Final Employee Records</h2>"

        for emp in employees:
            output += f"""
                Employee ID: {emp[0]}<br>
                Name: {emp[1]}<br>
                Department: {emp[2]}<br>
                Salary: ₹{emp[3]:.2f}<br>
                <hr>
            """

        return output

    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
