# routes/recommendations.py
from flask import Blueprint, request, jsonify
from services.recommendation_service import get_recommendations

bp = Blueprint('recommendations', __name__)

@bp.route('/recommendations', methods=['GET'])
def recommendations():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    recommendations = get_recommendations(user_id)
    return jsonify(recommendations)

