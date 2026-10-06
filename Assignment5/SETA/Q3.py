# Accept length and breadth through a form and calculate the area of a rectangle.

from flask import Flask, request

app = Flask(__name__)

@app.route("/area", methods=["GET", "POST"])
def area():
    if request.method == "POST":
        length = float(request.form.get("length"))
        breadth = float(request.form.get("breadth"))

        area = length * breadth
        return f"The area of the rectangle with length {length} and breadth {breadth} is: {area}"
    
    return '''
        <form method="post">
            Length: <input type="text" name="length"><br><br>
            Breadth: <input type="text" name="breadth"><br><br>
            <input type="submit" value="Calculate Area">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)