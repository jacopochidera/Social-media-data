from fastapi import APIRouter
from app.models import Post, AnalysisResponse
from app.services import analyze_sentiment, extract_keywords

analysis_router = APIRouter()

@analysis_router.post("/analyze", response_model=AnalysisResponse)
async def analyze_post(post: Post):
    sentiment = analyze_sentiment(post.content)
    keywords = extract_keywords(post.content)
    return AnalysisResponse(sentiment=sentiment, keywords=keywords)


