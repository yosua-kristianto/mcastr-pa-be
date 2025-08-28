from pydantic import BaseModel

class TextAnalysisFeedbackReviewRequestDTO(BaseModel):
    feedback_id: str