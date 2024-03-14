from flask import Flask, render_template, request, redirect
from models import Product, db

# ... (Instantiate app and db from database.py)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

# ... (Add routes for adding, editing, and deleting products)

if __name__ == '__main__':
    db.create_all()  # Create the database schema
    app.run(debug=True)