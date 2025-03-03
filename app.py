from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
from routes.feedback import bp as feedback_bp
from routes.movies import bp as movies_bp
from routes.preferences import bp as preferences_bp
from database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(feedback_bp)
    app.register_blueprint(movies_bp)
    app.register_blueprint(preferences_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)