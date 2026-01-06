from flask import Flask
from flask_cors import CORS
from config import db, migrate

app = Flask(__name__)
CORS(app)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///superheroes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)

# Import routes AFTER app is created
from routes import *

if __name__ == "__main__":
    app.run(debug=True, port=5555)
