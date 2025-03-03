import requests
from config import Config

# Cache genres at startup
GENRE_CACHE = {}
response = requests.get(f"https://api.themoviedb.org/3/genre/movie/list?api_key={Config.TMDB_API_KEY}&language=en-US")
if response.ok:
    GENRE_CACHE = {genre["id"]: genre["name"] for genre in response.json()["genres"]}

def fetch_tmdb_movies(endpoint):
    url = f"https://api.themoviedb.org/3/movie/{endpoint}?api_key={Config.TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if not response.ok:
        return [{"id": 0, "title": "Error", "genres": "N/A"}]  # Fallback
    data = response.json()["results"]
    return [
        {
            "id": movie["id"],
            "title": movie["title"],
            "genres": ",".join(GENRE_CACHE.get(id, "Unknown") for id in movie["genre_ids"])
        }
        for movie in data[:5]  # Limit to 5
    ]

def fetch_popular_movies():
    return fetch_tmdb_movies("popular")

def fetch_top_rated_movies():
    return fetch_tmdb_movies("top_rated")