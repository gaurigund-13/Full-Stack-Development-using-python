# Create a Flask application with an employee route that accepts an employee name 
#  through the URL and displays a personalized message.

from flask import Flask

app = Flask(__name__)

@app.route("/employee/<ename>")
def employee(ename):
    return f"Welcome to the Employee Page, {ename}!"

if __name__ == "__main__":
    app.run(debug=True)
