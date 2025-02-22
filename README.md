# Admin Interface for Product Management
======================================

## Description
---------------

This repository contains a Flask web application that provides an admin interface for managing products. The application uses a PostgreSQL database for data storage and retrieval. The project consists of two main Python files: `app.py` and `init_db.py`.

## Installation Instructions
---------------------------

To install and run the application, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine using Git.
2. **Install Requirements**: Install the required libraries by running `pip install -r requirements.txt` in your terminal.
3. **Setup Environment Variables**: Set the `PGpassword` environment variable with your PostgreSQL password.
4. **Initialize the Database**: Run `python init_db.py` to create the database tables.
5. **Run the Application**: Run `python app.py` to start the Flask development server.

## Usage Guide
--------------

1. **Access the Interface**: Open a web browser and navigate to `http://localhost:5000` to access the admin interface.
2. **Login**: No login is required for this basic implementation.
3. **Manage Products**: Use the interface to add, update, delete, and display products.

## Features
------------

* **Product Management**: Create, read, update, and delete products.
* **Validation and Error Handling**: Input validation and error handling for user input.
* **PostgreSQL Database**: Data storage and retrieval using a PostgreSQL database.

## Example Code Snippets
-----------------------

### Adding a Product

```python
from flask import request, jsonify
from app import app, db

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    # Validate input data
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400
    # Add product to database
    product = Product(name=data['name'], price=data['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'}), 201
```

### Retrieving Products

```python
from flask import jsonify
from app import app, db

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': product.id, 'name': product.name, 'price': product.price} for product in products])
```

## License
---------

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing
------------

Contributions are welcome! Please submit a pull request with your changes and a brief description of the changes made.

## Acknowledgments
----------------

* Flask: <https://flask.palletsprojects.com/en/2.0.x/>
* psycopg2: <https://www.psycopg.org/docs/>
* PostgreSQL: <https://www.postgresql.org/>
