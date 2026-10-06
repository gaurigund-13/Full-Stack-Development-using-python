# Create a Flask application that accepts two numbers through a form and displays their product.

from flask import Flask, request

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def home():
    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form['num2'])

        return f" Product of {num1} and {num2} is {num1*num2}"

    return f"""
       
<form method="post">
     
    num1:<input type="number" name="num1"><br><br>
    num2:<input type="number" name="num2"><br><br>

    <input type="submit" value="Product">
</form>

"""

app.run(debug=True)