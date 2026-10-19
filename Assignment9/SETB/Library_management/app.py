#  Q2. Create a Flask application to insert, display and update book details using Book_ID and 
# Display updated records.
from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

# Connect to database
def db_connect():
    return psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )

# Create Book table
def create_table():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Book (
            Book_ID SERIAL PRIMARY KEY,
            Title VARCHAR(100),
            Author VARCHAR(100),
            Price FLOAT
        )
    """)

    con.commit()
    cur.close()
    con.close()


# Insert book details
@app.route("/", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["Title"]
        author = request.form["Author"]
        price = request.form["Price"]

        con = db_connect()
        cur = con.cursor()

        cur.execute(
            "INSERT INTO Book (Title, Author, Price) VALUES (%s, %s, %s)",
            (title, author, price)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/")

    return render_template("add.html")


# Update and display books
@app.route("/update", methods=["GET", "POST"])
def update_book():
    con = db_connect()
    cur = con.cursor()

    if request.method == "POST":
        book_id = request.form["Book_ID"]
        price = request.form["Price"]

        cur.execute(
            "UPDATE Book SET Price = %s WHERE Book_ID = %s",
            (price, book_id)
        )

        con.commit()

    cur.execute("SELECT * FROM Book ORDER BY Book_ID")
    books = cur.fetchall()

    cur.close()
    con.close()

    return render_template("update.html", books=books)


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
