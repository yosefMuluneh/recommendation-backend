from models import Feedback
from services.tmdb_service import fetch_movie_details, fetch_popular_movies
from app import db, app

def get_recommendations(user_id):
    # Get user's highly rated movies (rating >= 4)
    high_rated = db.session.query(Feedback.movie_id).filter(Feedback.user_id == user_id, Feedback.rating >= 4).all()
    high_rated_ids = [id for (id,) in high_rated]

    if not high_rated_ids:
        # If no ratings, return popular movies
        popular_movies = fetch_popular_movies(app.config['TMDB_API_KEY'], page=1)
        return popular_movies[:10]

    # Get genres of high rated movies
    genres = set()
    for movie_id in high_rated_ids:
        movie_details = fetch_movie_details(app.config['TMDB_API_KEY'], movie_id)
        if 'genres' in movie_details:
            genres.update([genre['name'] for genre in movie_details['genres']])

    # Get a list of popular movies
    popular_movies = fetch_popular_movies(app.config['TMDB_API_KEY'], page=1)

    # Filter movies with at least one genre in common and not rated by user
    recommended = [
        movie for movie in popular_movies
        if any(genre['name'] in genres for genre in movie['genres']) and movie['id'] not in high_rated_ids
    ]

    # Sort by popularity
    recommended.sort(key=lambda x: x['popularity'], reverse=True)
    return recommended[:10]