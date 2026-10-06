from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form.get("name")
        feedback = request.form.get("feedback")

        return f"""
        <h2>Thank You {name}</h2>
        <p>Feedback: {feedback}</p>

        <br>
        <a href="/">Give Another Feedback</a>
        """

    return """
    <h2>Feedback Form</h2>

    <form method="POST">

        Name:
        <input type="text" name="name">
        <br><br>

        Feedback:
        <textarea name="feedback"></textarea>
        <br><br>

        <input type="submit" value="Submit">

    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)