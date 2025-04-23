from typing import List
import random

def analyze_sentiment(content: str) -> str:
    # A mock function to simulate sentiment analysis
    sentiments = ["positive", "negative", "neutral"]
    return random.choice(sentiments)

def extract_keywords(content: str) -> List[str]:
    # A mock function to simulate keyword extraction
    words = content.split()
    keywords = list(set(words))  # Unique words as keywords
    return keywords