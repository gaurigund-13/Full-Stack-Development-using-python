# Create a dynamic route that accepts a course name and displays course information.

from flask import Flask

app = Flask(__name__)

@app.route("/course/<course_name>")
def course_info(course_name):
    return f"Welcome to {course_name} course page"

if __name__ == '__main__':
    app.run(debug=True)