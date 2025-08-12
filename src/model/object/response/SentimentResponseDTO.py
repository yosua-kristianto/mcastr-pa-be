from pydantic import BaseModel

class SentimentRequestDTO(BaseModel):
    image_uri: str
    