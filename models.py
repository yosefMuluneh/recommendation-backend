from database import db

class User(db.Model):
    id = db.Column(db.String, primary_key=True)  # Firebase UID
    preferences = db.Column(db.String)  # Comma-separated genre IDs
    feedback = db.relationship("Feedback", backref="user")

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey("user.id"), nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)  # TMDB movie ID
    rating = db.Column(db.Float, nullable=True)  # User rating (1-5)
    comment = db.Column(db.String, nullable=True)
    sentiment_label = db.Column(db.String, nullable=True)
    sentiment_score = db.Column(db.Float, nullable=True)