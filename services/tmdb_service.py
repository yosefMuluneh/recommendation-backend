import requests
from config import Config
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Cache genres at startup
GENRE_CACHE = {}
response = requests.get(f"https://api.themoviedb.org/3/genre/movie/list?api_key={Config.TMDB_API_KEY}&language=en-US")
if response.ok:
    GENRE_CACHE = {genre["id"]: genre["name"] for genre in response.json()["genres"]}
else:
    logger.error(f"Failed to fetch genres: {response.status_code} - {response.text}")

def fetch_tmdb_movies(endpoint, genre_ids=None):
    base_url = "https://api.themoviedb.org/3"
    if endpoint.startswith("discover"):
        url = f"{base_url}/{endpoint}?api_key={Config.TMDB_API_KEY}&language=en-US&page=1"
    else:
        url = f"{base_url}/movie/{endpoint}?api_key={Config.TMDB_API_KEY}&language=en-US&page=1"
    if genre_ids:
        url += f"&with_genres={','.join(genre_ids)}"
    # logger.debug(f"Fetching from: {url}")
    response = requests.get(url)
    # if not response.ok:
    #     logger.error(f"API error: {response.status_code} - {response.text}")
    #     return [{"id": 0, "title": f"Error: {response.status_code}", "genres": "N/A", "poster_path": None}]
    data = response.json()
    results = data.get("results", [])
    logger.debug(f"API response: {results}")
    print(f"{endpoint} movies ========----=====", results[0])
    if not results:
        logger.warning(f"No results found in response: {data}")
    return [
        {
            "id": movie["id"],
            "title": movie["title"],
            "genres": ",".join(GENRE_CACHE.get(id, "Unknown") for id in movie["genre_ids"]),
            "poster_path": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get("poster_path") else None,
            "vote_average": movie.get("vote_average", 0),
            "release_date": movie.get("release_date", ""),
            "overview": movie.get("overview", "")
        }
        for movie in results[:5]
    ]

def fetch_popular_movies():
    return fetch_tmdb_movies("popular")

def fetch_top_rated_movies():
    return fetch_tmdb_movies("top_rated")

def fetch_movies_by_genres(genre_ids):
    return fetch_tmdb_movies("discover/movie", genre_ids)

def fetch_genre_list():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={Config.TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    if response.ok:
        return [{"id": genre["id"], "name": genre["name"]} for genre in response.json()["genres"]]
    return []