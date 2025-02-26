from models import Feedback
from services.sentiment_service import analyze_sentiment
from app import db

def submit_feedback(data):
    sentiment = analyze_sentiment(data['comment'])
    feedback = Feedback(
        user_id=data['user_id'],
        movie_id=data['movie_id'],
        rating=data['rating'],
        comment=data['comment'],
        sentiment_label=sentiment['label'],
        sentiment_score=sentiment['score']
    )
    db.session.add(feedback)
    db.session.commit()
    return {"message": "Feedback submitted", "sentiment": sentiment}