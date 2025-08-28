from fastapi import APIRouter, Depends
from sqlmodel import Session
from controller.text_analyzer.controller_handler import TextAnalyzerControllerHandler

from core.database import get_session
from model.object import BaseResponse
from model.object.request import TextAnalysisRequestDTO
from model.object.response import TextAnalysisResponseDTO

class TextAnalyzerController:

    router = APIRouter()

    @router.post("/")
    async def analyze_text(request: TextAnalysisRequestDTO, session: Session = Depends(get_session)):
        """This endpoint performs text analysis by taking the input text,
        and returning the CDN URL of an image that is related to the text based-on sentiment.

        -- Request:
        {
            "text": "I love programming!"
        }

        -- Response:

        {
            "image_uri": "https://cdn.example.com/images/sentiment/love.png"
            "feedback_id": "some-feedback-id"
        }

        """
        
        response: TextAnalysisRequestDTO = TextAnalyzerControllerHandler(session).handle_text_analysis(request.text)
        
        return BaseResponse.ok(
            message = "Text analysis completed", 
            data = response
        )


    async def feedback_review(request)