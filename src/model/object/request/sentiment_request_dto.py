from pydantic import BaseModel

class SentimentRequestDTO(BaseModel):
    text: str