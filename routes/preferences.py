from flask import Blueprint, request, jsonify
from models import User
from database import db

bp = Blueprint("preferences", __name__, url_prefix="/api/preferences")

@bp.route("", methods=["POST"])
def save_preferences():
    data = request.json
    user_id = data.get("user_id")
    genres = ",".join(str(g) for g in data.get("genres", []))  # Store as comma-separated genre IDs
    if not user_id or not genres:
        return jsonify({"error": "Missing user_id or genres"}), 400
    user = User.query.get(user_id)
    if not user:
        user = User(id=user_id, preferences=genres)
        db.session.add(user)
    else:
        user.preferences = genres
    db.session.commit()
    return jsonify({"message": "Preferences saved"})