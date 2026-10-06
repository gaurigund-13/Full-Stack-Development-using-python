# Create separate static routes for Employee, Department, and Contact pages.

from flask import Flask

app = Flask(__name__)

@app.route("/employee")
def employee():
    return "Welcome to Employee Page"

@app.route("/department")
def department():
    return "Welcome to Department Page"

@app.route("/contact")
def contact():
    return "Welcome to Contact Page"

if __name__ == "__main__":
    app.run(debug=True)
    