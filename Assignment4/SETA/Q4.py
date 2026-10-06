# Create Flask routes for /home, /student, and /faculty displaying suitable messages

from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "Welcome to Home Page"

@app.route("/student")
def student():
    return "Welcome to Student Page"

@app.route("/faculty")
def faculty():
    return "Welcome to Faculty Page"

if __name__ == "__main__":
    app.run(debug=True)
    