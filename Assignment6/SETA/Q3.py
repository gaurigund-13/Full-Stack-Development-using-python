# Create a Flask application to display student names in alphabetical order.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def student_list():
    
    students = ["Gauri", "Rahul", "Sneha", "Amit", "Priya"]

    sorted_students = sorted(students)

    student_names = "<br>".join(sorted_students)
    
    return f"""
    <h2>List of Students in Alphabetical Order</h2>
    {student_names}
    """

if __name__ == "__main__":
    app.run(debug=True)