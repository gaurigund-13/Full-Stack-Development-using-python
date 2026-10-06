# Q2. Create Contact and Services routes.

from flask import Flask

app = Flask(__name__)

@app.route("/contact")
def contact():
    return "Welcome to Contact Page"

@app.route("/services")
def services():
    return "Welcome to Services Page"

if __name__ == "__main__":
    app.run(debug=True)