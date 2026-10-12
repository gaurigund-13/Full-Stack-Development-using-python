# . Create a Flask application to display student details and calculate the total and average 
# marks dynamically.

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def student():

    if request.method == "POST":

        name = request.form.get("name")
        rollno = request.form.get("rollno")

        s1 = int(request.form.get("s1"))
        s2 = int(request.form.get("s2"))
        s3 = int(request.form.get("s3"))

        total = s1 + s2 + s3
        average = total / 3

        return f"""
        <h2>Student Details</h2>
        Name: {name}<br>
        Roll Number: {rollno}<br>
        Subject 1: {s1}<br>
        Subject 2: {s2}<br>
        Subject 3: {s3}<br>
        Total Marks: {total}<br>
        Average Marks: {average:.2f}<br><br>

        <a href="/">Enter Another Student</a>
        """

    return """
    <h2>Student Marks Form</h2>

    <form method="POST">

        Name: <input type="text" name="name" required>
        <br><br>

        Roll Number: <input type="text" name="rollno" required>
        <br><br>

        Subject 1 Marks: <input type="number" name="s1" min="0" max="100" required>
        <br><br>

        Subject 2 Marks: <input type="number" name="s2" min="0" max="100" required>
        <br><br>

        Subject 3 Marks: <input type="number" name="s3" min="0" max="100" required>
        <br><br>

        <input type="submit" value="Calculate">

    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)