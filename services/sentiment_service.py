from transformers import pipeline

# Load pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(comment):
    result = sentiment_pipeline(comment)[0]
    return {
        "label": result["label"],
        "score": result["score"]
    }