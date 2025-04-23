from pydantic import BaseModel
from typing import List

class Post(BaseModel):
    username: str
    content: str

class AnalysisResponse(BaseModel):
    sentiment: str
    keywords: List[str]