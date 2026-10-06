# Create a Flask application to display a birthday message along with the current date.

from flask import Flask
from datetime import date
app = Flask(__name__)

@app.route("/")
def home(): 
    return f"<h1>Happy Birthday</h1> Today is {date.today().strftime("Date: %d-%m-%Y")}"

if __name__ == "__main__":
    app.run(debug=True)