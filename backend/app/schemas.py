from pydantic import BaseModel, Field


class ProgressUpdate(BaseModel):
    completed: bool


class QuizSubmission(BaseModel):
    answers: list[int]


class JournalCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    body: str = Field(min_length=1, max_length=5000)
