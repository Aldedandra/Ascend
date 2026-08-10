from pydantic import BaseModel, Field


class ProgressUpdate(BaseModel):
    completed: bool


class QuizSubmission(BaseModel):
    answers: list[int]


class JournalCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    body: str = Field(min_length=1, max_length=5000)


class ElevenLabsPreviewRequest(BaseModel):
    voice_id: str = Field(min_length=1, max_length=128)
    text: str = Field(min_length=20, max_length=600)
    model_id: str | None = Field(default=None, max_length=80)


class ElevenLabsLessonAudioRequest(BaseModel):
    narrator_id: str = Field(default="bella", pattern="^(bella|brian)$")
