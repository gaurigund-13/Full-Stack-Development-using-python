# Q3. Create a Flask application for a simple library search system that accepts a book name 
# and displays the search result.

from flask import Flask, request

app = Flask(__name__)

books = ["Python", "Java","C++","JavaScript"]
@app.route('/search', methods = ['GET','POST'])
def search():
    if request.method == "POST":

        bname = request.form.get("bname")

        if bname in books:
            result = f"Book found : {bname}"
        else:
            result = f" Book not found : {bname}"

        return f"""
        <h2>Search Result </h2>
        <p>{result}</p>
      """

    return """
    <h2>Library Search</h2>

    <form method="POST">

        Name:
        <input type="text" name="bname">
        <br><br>

        <input type="submit" value="Search">

    </form>
    """

app.run(debug=True)