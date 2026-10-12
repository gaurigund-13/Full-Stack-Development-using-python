# Create a Flask application to display the details of five employes stored in a Python list.


from flask import Flask

app = Flask(__name__)

@app.route("/")
def employee_list():

    employees = [
        ("Rahul Sharma", "IT", 45000),
        ("Priya Patil", "HR", 40000),
        ("Amit Shrivastav", "Finance", 50000),
        ("Sneha Roy", "Marketing", 42000),
        ("Vikram Varma", "IT", 55000)
    ]

    employee_details = ""

    for name, department, salary in employees:
        employee_details += f"""
        <p>
            Name: {name}<br>
            Department: {department}<br>
            Salary: ₹{salary}
        </p>
        <hr>
        """

    return f"""
    <h2>List of Employees</h2>
    {employee_details}
    """

if __name__ == "__main__":
    app.run(debug=True)
