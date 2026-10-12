# Q1. Product Management API
# Create a Flask application.
# Requirements:
# 1. Create a GET API /products that returns details of at least 3 products. 
# 2. Create a POST API /addproduct that accepts Product Name and Price. 
# 3. Test both APIs using Postman and verify the responses. 
# Sample Product:
# {
#  "name":"Laptop",
# 20
#  "price":50000
# }

from flask import Flask ,request, jsonify

app = Flask(__name__)

products = [
    {"name":"Laptop", "Price": 50000, "Category":"Electronic"},
    {"name":"Mobile", "Price": 40000, "Category":"Electronic"},
    {"name":"Mackbook", "Price": 100000, "Category":"Electronic"},

]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route("/addproducts", methods = ["POST"])
def add_product():

    data = request.get_json()

    name = data.get("name")
    price = data.get("price")

    product = {
        "name":name,
        "price":price
    }

    products.append(product)

    return jsonify(
        {
            "msg":"Product added sucessfully",
            "product":product
        }
    ),201

if __name__ == '__main__':
    app.run(debug = True)