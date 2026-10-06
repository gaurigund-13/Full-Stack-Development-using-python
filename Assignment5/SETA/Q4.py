# Accept a student's marks and display Pass or Fail based on the entered marks.

from flask import Flask, request

app = Flask(__name__)

@app.route("/marks", methods=["GET", "POST"])
def marks():
    if request.method == "POST":
        marks = int(request.form.get("marks"))
        if marks >= 35:
            return f"Congratulations! You have passed with {marks} marks."
        else:
            return f"Sorry! You have failed with {marks} marks."
    
    return '''
        <form method="post">
            Marks: <input type="text" name="marks"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
    