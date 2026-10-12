# Display employee details stored in a Python list.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def employee_list():

    employees = [
        ("Rahul Sharma", "IT", 45000),
        ("Priya Patil", "HR", 40000),
        ("Amit Sharma", "Finance", 50000),
        ("Sneha Roy", "Marketing", 42000),
        ("Vikram Verma", "IT", 55000)
    ]

    result = "<h2>Employee Details</h2>"

    for name, department, salary in employees:
        result += f"""
            Name  : {name}<br>
            Department : {department}<br>
            Salary : ₹{salary}<br><br>
        """
    return result

if __name__ == "__main__":
    app.run(debug=True)