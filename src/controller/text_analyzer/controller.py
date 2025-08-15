from fastapi import APIRouter
from controller_handler import handle_text_analysis

from model.object.base_response_dto import BaseResponse
from model.object.request.sentiment_request_dto import SentimentRequestDTO
from model.object.response.sentiment_response_dto import SentimentResponseDTO

class TextAnalyzerController:

    router = APIRouter()

    @router.post("/")
    async def analyze_text(request: SentimentRequestDTO):
        """This endpoint performs text analysis by taking the input text,
        and returning the CDN URL of an image that is related to the text based-on sentiment.
        """
        
        response = SentimentResponseDTO()
        response.image_uri = handle_text_analysis(request.text)
        
        return BaseResponse.ok(
            message = "Text analysis completed", 
            data = response
        )