from app import db

class User(db.Model):
    id = db.Column(db.String, primary_key=True)  # Firebase UID
    email = db.Column(db.String, unique=True, nullable=False)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # TMDB movie ID
    title = db.Column(db.String, nullable=False)
    genres = db.Column(db.String, nullable=True)
    poster_url = db.Column(db.String, nullable=True)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    comment = db.Column(db.String, nullable=True)
    sentiment_label = db.Column(db.String, nullable=True)
    sentiment_score = db.Column(db.Float, nullable=True)