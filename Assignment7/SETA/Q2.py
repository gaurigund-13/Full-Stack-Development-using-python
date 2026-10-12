# Q2. Employee Information API
# Create a Flask application.
# Requirements:
# 1. Create a GET API /employee that returns employee details. 
# 2. Create a POST API /addemployee that accepts Employee Name and 
# Department. 
# 3. Test both APIs using Postman.

from flask import Flask ,request, jsonify

app = Flask(__name__)

employee =[ ]


@app.route('/employee',methods=['GET'])
def get_employee():
    return jsonify(employee)
  
@app.route('/addemployee', methods=['POST'])
def add_employee():

    data = request.get_json()

    employee.append(data)

    return jsonify(
        {
            "msg":"Employee added sucessfully",
            "employee":data
        }
    )

if __name__ == '__main__':
    app.run(debug = True)