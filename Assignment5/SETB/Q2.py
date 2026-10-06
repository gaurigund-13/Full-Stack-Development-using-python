# Create a feedback form using Name, Rating, and Comments and display the submitted feedback.

from flask import Flask, request

app = Flask(__name__)

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("name")
        rating = request.form.get("rating")
        comments = request.form.get("comments")

        return f"""
        Feedback Submitted:
        <p>
            Name: {name}<br>
            Rating: {rating}<br>
            Comments: {comments}
        </p>
        """
    
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Rating: <input type="text" name="rating"><br>
            Comments: <textarea name="comments"></textarea><br>
            <input type="submit" value="Submit Feedback">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
    