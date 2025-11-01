from fastapi import APIRouter, Depends
from sqlmodel import Session
from controller.text_analyzer.controller_handler import TextAnalyzerControllerHandler

from core.database import get_session
from model.object import BaseResponse
from model.object.request import TextAnalysisRequestDTO, TextAnalysisFeedbackReviewRequestDTO, TextAnalysisFeedbackReviewSubmissionRequestDTO
from model.object.response import TextAnalysisResponseDTO, TextAnalysisFeedbackReviewResponseDTO


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

    @router.post("/feedback/review")
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

        response: TextAnalysisFeedbackReviewResponseDTO = await TextAnalyzerControllerHandler(session).handle_feedback_review(request.feedback_id)

        tidy_response = {
            "data_0": {
                "image_uri": response.ressemblance_0,
                "choice_id": 0
            },
            "data_1": {
                "image_uri": response.ressemblance_1,
                "choice_id": 1
            },
            "data_2": {
                "image_uri": response.ressemblance_2,
                "choice_id": 2
            },
            "data_3": {
                "image_uri": response.ressemblance_3,
                "choice_id": 3
            },
            "data_4": {
                "image_uri": response.ressemblance_4,
                "choice_id": 4
            },
            "data_5": {
                "image_uri": response.ressemblance_5,
                "choice_id": 5
            }
        }

        return BaseResponse.ok(message = "Feedback Provided", data = tidy_response)

    @router.post("/feedback/submit")
    async def feedback_review_submission(request: TextAnalysisFeedbackReviewSubmissionRequestDTO, session: Session = Depends(get_session)):
        """This endpoints submits feedback review.

        -- Request:
        {
            "feedback_id": "some-feedback-uuid",
            "submission": 1
        }

        -- Response:
        {
            "feedback_id": "some-feedback-uuid"
        }

        """
        await TextAnalyzerControllerHandler(session).handle_feedback_submission(request.feedback_id, request.review_id)
        return BaseResponse.ok(message = "Feedback successfully submitted", data = {
            "feedback_id": request.feedback_id
        })
