from fastapi import APIRouter, Depends
from sqlmodel import Session
from controller.text_analyzer.controller_handler import TextAnalyzerControllerHandler

from core.database import get_session
from model.object import BaseResponse
from model.object.request import TextAnalysisRequestDTO, TextAnalysisFeedbackReviewRequestDTO
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
        
        response: TextAnalysisRequestDTO = await TextAnalyzerControllerHandler(session).handle_text_analysis(request.text)
        
        return BaseResponse.ok(
            message = "Text analysis completed", 
            data = response
        )


    async def feedback_review(request: TextAnalysisFeedbackReviewRequestDTO, session: Session = Depends(get_session)):
        """This endpoints triggers feedback review options. Providing a multiple choices
        that is based-on randomized value from pic repository.

        -- Request:
        {
            "feedback_id": "some-feedback-uuid"
        }

        -- Response:
        {
            "0": "some_cdn/path/to/image.jpg",
            "1": "some_cdn/path/to/image.jpg",
            "2": "some_cdn/path/to/image.jpg",
            "3": "some_cdn/path/to/image.jpg",
            "4": "some_cdn/path/to/image.jpg",
            "5": "some_cdn/path/to/image.jpg",
        }

        """