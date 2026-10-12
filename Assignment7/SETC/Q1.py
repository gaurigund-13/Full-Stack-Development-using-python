# Q1. Student Result API
# Create a Flask application.
# Requirements:
# 1. Create a GET API /result that displays sample student result data. 
# 2. Create a POST API /addresult that accepts: 
#  Student Name & Marks 
# 3. Return: 
# o Student Name 
# o Marks 
# 4. Result (Pass if Marks ≥ 40 else Fail) Test both APIs using 
# Postman.
# Sample Input:
# {
#  "name":"Priya",
#  "marks":75
# }
# Sample Output:
# {
#  "name":"Priya",
#  "marks":75,
#  "result":"Pass"
# }

from flask import Flask ,request, jsonify

app = Flask(__name__)

@app.route("/result", methods=["GET"])
def get_result():

    students = [
        {"name": "Gauri", "marks": 85, "result": "Pass"},
        {"name": "Rahul", "marks": 35, "result": "Fail"},
        {"name": "Sneha", "marks": 60, "result": "Pass"}
    ]

    return jsonify(students)


@app.route("/addresult", methods=["POST"])
def add_result():

    data = request.get_json()

    name = data.get("name")
    marks = data.get("marks")

    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return jsonify({
        "name": name,
        "marks": marks,
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)