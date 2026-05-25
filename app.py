from flask import Flask, jsonify, request, abort

app = Flask(__name__)

products = {}
next_product_id = 1


def validate_product_data(data, is_update=False):
    """
    Validate product input data.
    Returns (is_valid, error_message)
    """
    if not data:
        return False, 'Request body must be JSON'
    
    # For create (POST), both fields are required
    if not is_update:
        if 'name' not in data:
            return False, 'Product must include name'
        if 'price' not in data:
            return False, 'Product must include price'
    
    # Validate name if provided
    if 'name' in data:
        if not isinstance(data['name'], str) or not data['name'].strip():
            return False, 'Name must be a non-empty string'
    
    # Validate price if provided
    if 'price' in data:
        try:
            price = float(data['price'])
            if price <= 0:
                return False, 'Price must be a positive number'
        except (TypeError, ValueError):
            return False, 'Price must be a valid number'
    
    return True, None

@app.route('/products', methods=['POST'])
def create_product():
    global next_product_id
    
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.get_json(silent=True)
    
    is_valid, error_message = validate_product_data(data, is_update=False)
    if not is_valid:
        return jsonify({'error': error_message}), 400

    product = {
        'id': next_product_id,
        'name': data['name'].strip(),
        'price': float(data['price'])
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

    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    data = request.get_json(silent=True)
    
    is_valid, error_message = validate_product_data(data, is_update=True)
    if not is_valid:
        return jsonify({'error': error_message}), 400

    if 'name' in data:
        product['name'] = data['name'].strip()
    if 'price' in data:
        product['price'] = float(data['price'])

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

