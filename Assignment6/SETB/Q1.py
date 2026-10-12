# Display student information stored in dictionary.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def student_info():
    student = {
        "name": "Gauri Gund",
        "rollno": "101",
        "age" : 24,
        "class" : "S.Y.M.Sc.(CS)"
    }

    return f"""
    <h2>Student Information</h2>
    Name: {student['name']}<br>
    Roll Number: {student['rollno']}<br>
    Age: {student['age']}<br>
    Class: {student['class']}<br>
   
    """

if __name__ == "__main__":
    app.run(debug=True)