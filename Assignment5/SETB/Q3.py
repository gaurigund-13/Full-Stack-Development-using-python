# Accept employee basic salary and calculate the total salary after adding a fixed allowance.

from flask import Flask, request

app = Flask(__name__)

@app.route("/salary", methods=["GET", "POST"])
def salary():

    if request.method == "POST":

        basic_salary = float(request.form.get("basic_salary"))
        allowance = 5000  
        total_salary = basic_salary + allowance
        return f"The total salary after adding a fixed allowance of {allowance} to the basic salary of {basic_salary} is: {total_salary}"
    
    return '''
        <form method="post">
            Basic Salary: <input type="text" name="basic_salary"><br><br>
            <input type="submit" value="Calculate Total Salary">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
    