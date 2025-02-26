# backend/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Import and register blueprints
from routes import recommendations, feedback
app.register_blueprint(recommendations.bp)
app.register_blueprint(feedback.bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)