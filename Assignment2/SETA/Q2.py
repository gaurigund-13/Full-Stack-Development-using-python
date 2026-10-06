# Create a Flask application displaying "Welcome to Flask".

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Welcome to the Flask"

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask"

if __name__ == "__main__":
    app.run(debug=True)