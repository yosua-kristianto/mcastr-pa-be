from pydantic import BaseModel

class SentimentRequestDTO(BaseModel):
    test: str