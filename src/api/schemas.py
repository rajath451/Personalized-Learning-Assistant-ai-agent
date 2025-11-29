from pydantic import BaseModel
from typing import List, Optional

class QuizSchema(BaseModel):
    question: str
    options: List[str]
    correct_answer: str

class ExplanationSchema(BaseModel):
    topic: str
    explanation: str
    examples: Optional[List[str]] = None

class ScheduleSchema(BaseModel):
    user_id: str
    study_sessions: List[str]  # List of study session times in ISO format

class UserProfileSchema(BaseModel):
    user_id: str
    preferences: dict  # User preferences for learning styles, topics, etc.

class ContentMetadataSchema(BaseModel):
    content_id: str
    title: str
    description: str
    tags: List[str]  # Tags for categorizing content