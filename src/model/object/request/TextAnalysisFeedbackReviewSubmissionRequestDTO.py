from pydantic import BaseModel


class TextAnalysisFeedbackReviewSubmissionRequestDTO(BaseModel):
    feedback_id: str
    review_id: int