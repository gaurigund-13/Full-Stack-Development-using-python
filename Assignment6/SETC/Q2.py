# Create a Flask application to display students who have scored more than 60 marks.

from flask import Flask

app = Flask(__name__)

@app.route("/students")
def students():

    students = [
        ("Gauri", 85),
        ("Rohit", 45),
        ("Sakshi", 75),
        ("Amit", 55),
        ("Priya", 95)
    ]

    result = "<h2>Students Scorign more than 60 Marks</h2>"

    for name, marks in students:
        if marks >= 60:
            result += f"{name} - {marks} marks <br>"

    return result

if __name__ == "__main__":
    app.run(debug=True)
    


            