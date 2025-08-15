from pydantic import BaseModel

class SentimentResponseDTO(BaseModel):
    image_uri: str
    