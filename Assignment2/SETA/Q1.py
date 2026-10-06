# Demonstrate a GET request using browser and explain the response

from flask import Flask, request
app=Flask(__name__)

@app.route("/student", methods=["GET"])
def student():
    return "Student details received using GET request."

if __name__ == "__main__": 
    app.run(debug=True)