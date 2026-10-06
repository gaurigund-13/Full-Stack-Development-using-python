# Accept employee details and display entered information.

from flask import Flask, request

app = Flask(__name__)

@app.route("/employee", methods=["GET", "POST"])
def employee():

    if request.method == "POST":

        eid = request.form.get("eid")
        name = request.form.get("name")
        age = request.form.get("age")
        department = request.form.get("department")
        return f"""
        Employee Details:
        <p>
            EMP_ID:{eid}<br>
            Name: {name}<br>
            Age: {age}<br>
            Department: {department}
        </p>

        """
    
    return '''
        <form method="post">
            eid: <input type="text" name="eid"><br>
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br>
            Department: <input type="text" name="department"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
