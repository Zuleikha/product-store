"""Test script for Flask CRUD API validation"""
import json
from app import app

def test_api():
    client = app.test_client()
    
    print("=" * 60)
    print("TESTING INPUT VALIDATION")
    print("=" * 60)
    
    # Test 1: Missing name
    print("\n1. Create product WITHOUT name:")
    response = client.post('/products', 
        json={'price': 19.99},
        content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    
    # Test 2: Missing price
    print("\n2. Create product WITHOUT price:")
    response = client.post('/products',
        json={'name': 'Laptop'},
        content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    
    # Test 3: Empty name string
    print("\n3. Create product with EMPTY name:")
    response = client.post('/products',
        json={'name': '   ', 'price': 19.99},
        content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    
    # Test 4: Non-string name
    print("\n4. Create product with NON-STRING name:")
    response = client.post('/products',
        json={'name': 123, 'price': 19.99},
        content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    
    # Test 5: Zero price
    print("\n5. Create product with ZERO price:")
    response = client.post('/products',
        json={'name': 'Laptop', 'price': 0},
        content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    
    # Test 6: Negative price
    print("\n6. Create product with NEGATIVE price:")
    response = client.post('/products',
        json={'name': 'Laptop', 'price': -50},
        content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    
    # Test 7: Invalid price (non-numeric)
    print("\n7. Create product with INVALID price (non-numeric):")
    response = client.post('/products',
        json={'name': 'Laptop', 'price': 'expensive'},
        content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    
    # Test 8: Valid product
    print("\n8. Create product with VALID data:")
    response = client.post('/products',
        json={'name': 'Laptop', 'price': 999.99},
        content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    product_id = response.get_json().get('id')
    
    # Test 9: Update with invalid name
    print("\n9. Update product with INVALID name (empty):")
    response = client.put(f'/products/{product_id}',
        json={'name': ''},
        content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    
    # Test 10: Update with invalid price (zero)
    print("\n10. Update product with INVALID price (zero):")
    response = client.put(f'/products/{product_id}',
        json={'price': 0},
        content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    
    # Test 11: Valid update
    print("\n11. Update product with VALID data:")
    response = client.put(f'/products/{product_id}',
        json={'name': 'Gaming Laptop', 'price': 1299.99},
        content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    
    # Test 12: No JSON body
    print("\n12. Create product with NO JSON body:")
    response = client.post('/products',
        content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED")
    print("=" * 60)

if __name__ == '__main__':
    test_api()
