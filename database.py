from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize without app

def init_app(app):  # Function to initialize later
    db.init_app(app)