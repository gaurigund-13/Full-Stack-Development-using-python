# Q2. Create a POST API /order to accept Product Name, Price and Quantity and return the 
# order details with total amount.

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/order", methods = ["POST"])
def add_orders():

    data = request.get_json()

    name = data.get("name")
    price = data.get("price")
    quantity = data.get("quantity")

    total = price* quantity

    return jsonify({
        "name":name,
        "price":price,
        "quantity":quantity,
        "total":total
    })

if __name__ == '__main__':
    app.run(debug = True)
    