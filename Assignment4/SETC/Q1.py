# Create dynamic route accepting product ID and displaying product details.

from flask import Flask

app = Flask(__name__)

@app.route("/product/<int:product_id>")
def product_details(product_id):
    return f"Details of product with ID: {product_id}"

if __name__ == "__main__":
    app.run(debug=True)
    