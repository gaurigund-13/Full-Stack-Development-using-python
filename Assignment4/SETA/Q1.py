# Create Home and About routes.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return " Welcome to Home Page"

@app.route('/about')
def about():
    return "Welcome to About Page"

if __name__ == "__main__":
    app.run(debug=True)