# Q4. Create a Flask application with a login form and display "Login Successful" when valid 
# details are submitted.

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            return "<h2>Login Successful</h2>"
        else:
            return "<h2>Invalid Credentials</h2>"

    return """
    <h2>Login Form</h2>

    <form method="POST">

        Username:
        <input type="text" name="username">
        <br><br>

        Password:
        <input type="password" name="password">
        <br><br>

        <input type="submit" value="Login">

    </form>
    """

app.run(debug=True)