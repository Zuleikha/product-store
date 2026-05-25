from flask import Flask, jsonify, request, abort

app = Flask(__name__)

products = {}
next_product_id = 1

@app.route('/products', methods=['POST'])
def create_product():
    global next_product_id
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Product must include name and price'}), 400

    try:
        price = float(data['price'])
    except (TypeError, ValueError):
        return jsonify({'error': 'Price must be a number'}), 400

    product = {
        'id': next_product_id,
        'name': data['name'],
        'price': price
    }
    products[next_product_id] = product
    next_product_id += 1
    return jsonify(product), 201

@app.route('/products', methods=['GET'])
def list_products():
    return jsonify(list(products.values()))

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product)

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body must be JSON'}), 400

    if 'name' in data:
        product['name'] = data['name']
    if 'price' in data:
        try:
            product['price'] = float(data['price'])
        except (TypeError, ValueError):
            return jsonify({'error': 'Price must be a number'}), 400

    products[product_id] = product
    return jsonify(product)

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id not in products:
        return jsonify({'error': 'Product not found'}), 404
    deleted = products.pop(product_id)
    return jsonify(deleted)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

