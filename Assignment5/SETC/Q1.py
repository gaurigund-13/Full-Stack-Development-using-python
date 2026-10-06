# Create a simple login form and validate entered username.

from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "gauri" and password == "1234":
            return f"Welcome {username}! You have successfully logged in."
        else:
            return "Invalid username or password. Please try again."
    
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
    