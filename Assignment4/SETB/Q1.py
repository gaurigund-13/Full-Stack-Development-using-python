# Create dynamic route accepting student name.

from flask import Flask

app = Flask(__name__)

@app.route("/student/<name>")
def student_info(name):
    return f"Welcome {name} to the Student Page"

if __name__ == "__main__":
    app.run(debug=True)
    