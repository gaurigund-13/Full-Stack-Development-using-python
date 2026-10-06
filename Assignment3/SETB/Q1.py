# Q1. Create a Flask application displaying current date and time.

from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def home(): 
    return datetime.now().strftime("Date: %d-%m-%Y<br>Time: %H:%M:%S")

if __name__ == "__main__":
    app.run(debug=True)