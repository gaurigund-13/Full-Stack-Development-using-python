# Q1. Student Information API
# Create a Flask application.
# Requirements:
# 1. Create a GET API /student that returns student details in JSON format. 
# 2. Create a POST API /addstudent that accepts Student Name and Course. 
# 3. Test both APIs using Postman. 
# Sample GET Output:
# {
#  "name":"Rahul",
#  "course":"BSc IT"
# }

from flask import Flask ,request, jsonify

app = Flask(__name__)

students =[ ]


@app.route('/student',methods=['GET'])
def get_student():
    return jsonify(students)
  
@app.route('/student', methods=['POST'])
def add_student():

    data = request.get_json()

    students.append(data)

    return jsonify(
        {
            "msg":"Student added sucessfully",
            "student":data
        }
    )

if __name__ == '__main__':
    app.run(debug = True)