# routes/feedback.py
from flask import Blueprint, request, jsonify
from services.feedback_service import submit_feedback

bp = Blueprint('feedback', __name__)

@bp.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    if not all(key in data for key in ['user_id', 'movie_id', 'rating', 'comment']):
        return jsonify({"error": "Missing required fields"}), 400
    result = submit_feedback(data)
    return jsonify(result)