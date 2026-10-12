# Create a Flask application to display a list of five student names dynamically.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def student_list():

    students = ["Gauri", "Rahul", "Sneha", "Amit", "Priya"]

    student_names = "<br>".join(students)
    
    return f"""
    <h2>List of Students</h2>
    {student_names}
    """

if __name__ == "__main__":
    app.run(debug=True)