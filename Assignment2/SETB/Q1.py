from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        uname = request.form.get("uname")
        passwd = request.form.get("passwd")

        return f"""
        <h2>Login Successfully</h2>
        """

    return """
    <h2>Login Form</h2>

    <form method="POST">

        Username:
        <input type="text" name="uname">
        <br><br>

        Password:
        <input type="password" name="passwd">
        <br><br>

        <input type="submit" value="Login">

    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)