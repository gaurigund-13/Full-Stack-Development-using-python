# Create a simple product order form accepting Product Name, Quantity, and Price and display the order details.

from flask import Flask, request

app = Flask(__name__)

@app.route("/product", methods=["GET", "POST"])
def product():

    if request.method == "POST":
        product_name = request.form.get("product_name")
        quantity = request.form.get("quantity")
        price = request.form.get("price")

        return f"""
        Order Details:
        <p>
            Product Name: {product_name}<br>
            Quantity: {quantity}<br>
            Price: {price}
        </p>
        """

if __name__ == '__main__':
    app.run(debug=True)
