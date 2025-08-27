from fastapi import APIRouter, Depends
from sqlmodel import Session
from controller.text_analyzer.controller_handler import TextAnalyzerControllerHandler

from core.database import get_session
from model.object.base_response_dto import BaseResponse
from model.object.request.sentiment_request_dto import SentimentRequestDTO
from model.object.response.sentiment_response_dto import SentimentResponseDTO

class TextAnalyzerController:

    router = APIRouter()

    @router.post("/")
    async def analyze_text(request: SentimentRequestDTO, session: Session = Depends(get_session)):
        """This endpoint performs text analysis by taking the input text,
        and returning the CDN URL of an image that is related to the text based-on sentiment.

        -- Request:
        {
            "text": "I love programming!"
        }

        -- Response:

        {
            "image_uri": "https://cdn.example.com/images/sentiment/love.png"
        }

        """
        
        response = SentimentResponseDTO()

        response.image_uri = TextAnalyzerControllerHandler(session).handle_text_analysis(request.text)
        
        return BaseResponse.ok(
            message = "Text analysis completed", 
            data = response
        )