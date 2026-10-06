# Create a Flask application displaying your name and roll number.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Name: Samarth, Roll Number: 12"

if __name__ == '__main__':
    app.run(debug=True)