# . Accept two numbers and display its addition.

from flask import Flask, request

app = Flask(__name__)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        num1 = int(request.form.get("num1"))
        num2 = int(request.form.get("num2"))

        sum =num1 +num2
        return f"The sum of {num1} and {num2} is: {sum}"
        
    
    return '''
        <form method="post">
            Number 1: <input type="text" name="num1"><br>
            Number 2: <input type="text" name="num2"><br>
            <input type="submit" value="Add">
        </form>
    '''