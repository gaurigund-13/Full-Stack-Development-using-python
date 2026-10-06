# Create a basic Flask application and display "Hello, Students" in the browser.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Students"

if __name__ == '__main__':
    app.run(debug=True)