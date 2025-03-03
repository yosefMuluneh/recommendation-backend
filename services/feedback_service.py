from models import Feedback
from services.sentiment_service import analyze_sentiment
from database import db

def submit_feedback(data):
    sentiment = analyze_sentiment(data["comment"]) if data.get("comment") else {"label": None, "score": None}
    feedback = Feedback(
        user_id=data["user_id"],
        movie_id=data["movie_id"],
        comment=data.get("comment"),
        sentiment_label=sentiment["label"],
        sentiment_score=sentiment["score"]
    )
    db.session.add(feedback)
    db.session.commit()
    return {"message": "Feedback submitted", "sentiment": sentiment}