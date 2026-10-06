# Q1. Create a Flask application displaying a simple message about your college department.

from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Welcome to the Information Technology Department"

app.run(debug=True)