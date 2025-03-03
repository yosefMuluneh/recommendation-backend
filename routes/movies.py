from flask import Blueprint, request, jsonify
from services.tmdb_service import fetch_popular_movies, fetch_top_rated_movies, fetch_genre_list
from services.recommendation_service import get_recommendations
from models import User

bp = Blueprint("movies", __name__, url_prefix="/api/movies")

@bp.route("/recommendations", methods=["GET"])
def recommendations():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400
    user = User.query.get(user_id)
    if not user or not user.preferences:
        return jsonify({
            "message": "No preferences found, returning popular movies",
            "recommendations": fetch_popular_movies()
        }), 200
    recs = get_recommendations(user.preferences)
    return jsonify(recs)

@bp.route("/popular", methods=["GET"])
def popular():
    popular_movies = jsonify(fetch_popular_movies())
    return popular_movies

@bp.route("/top-rated", methods=["GET"])
def top_rated():
    topratedMovies = fetch_top_rated_movies()
    print("toprated movies ------==-----======", topratedMovies[0])
    topratedMovies = jsonify(topratedMovies)
    return topratedMovies

@bp.route("/genres", methods=["GET"])
def genres():
    return jsonify(fetch_genre_list())