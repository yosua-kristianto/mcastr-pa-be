from pydantic import BaseModel

class TextAnalysisRequestDTO(BaseModel):
    text: str