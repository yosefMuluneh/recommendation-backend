from services.tmdb_service import fetch_movies_by_genres

def get_recommendations(user_preferences):
    genre_ids = user_preferences.split(",")
    # return fetch_movies_by_genres(genre_ids)
    return []