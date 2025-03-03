from flask import Blueprint, request, jsonify
from services.feedback_service import submit_feedback

bp = Blueprint("feedback", __name__, url_prefix="/api/feedback")

@bp.route("", methods=["POST"])
def feedback():
    data = request.json
    required = ["user_id", "movie_id", "comment"]
    if not all(key in data for key in required):
        return jsonify({"error": "Missing required fields"}), 400
    result = submit_feedback(data)
    return jsonify(result)
