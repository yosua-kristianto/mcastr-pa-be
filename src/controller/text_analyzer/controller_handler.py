from sqlmodel import Session
from common.constant import GCO_MODEL_TYPE_SWITCH_CONFIG_KEY, LGBM_MODEL_VERSION, SVC_MODEL_VERSION
from core.model_integrator import EmoAnalyzerModel
from model.entity import ModelVersion
from model.entity import ModelLog

import uuid

from model.object.response import TextAnalysisFeedbackReviewResponseDTO
from model.object.response.TextAnalysisResponseDTO import TextAnalysisResponseDTO
from repository.gco import ConfigRepository
from repository.ml import EmotionPicRepository
from repository.mlops import ModelLogRepository


class TextAnalyzerControllerHandler:

    def __init__(self, session: Session):
        self.config_repository = ConfigRepository(session)
        self.model_log_repository = ModelLogRepository(session)
        self.emotion_pic_repository = EmotionPicRepository(session)

    async def handle_text_analysis(self, text: str) -> TextAnalysisResponseDTO:
        """This handler function processes as bridge input text to perform sentiment analysis, 
        and take control of the logic to return the CDN URL of an image related to the sentiment of the text.

        The sentiment analysis logic is applied in the ML dedicated service layer.

        Args:
            text (str): The input text to analyze.

        Returns:
            str: The CDN URL of the image related to the sentiment of the text.
        """

        model_configuration = self.config_repository.get_config_by_key(GCO_MODEL_TYPE_SWITCH_CONFIG_KEY)

        prediction = EmoAnalyzerModel(model_configuration).emo_analysis(text)

        model_log = ModelLog()
        model_log.uuid = str(uuid.uuid4())
        model_log.version_id = LGBM_MODEL_VERSION if model_configuration == "lgb" else SVC_MODEL_VERSION
        model_log.user_session_id = "some-session-id"
        model_log.prompt = text
        model_log.model_output = prediction

        self.model_log_repository.create_model_log(model_log)


        return TextAnalysisResponseDTO(
            image_uri=self.emotion_pic_repository.get_emotion_pic_by_emotion_flag(prediction),
            feedback_id=model_log.uuid
        )

    def handle_feedback_review(self, feedback_id: str):
        """This function handles getting review as follows:
        
        1. Verify whether this feedback is already reviewed. If reviewed, throw exception
        2. Return the feedback.
        
        """
        model_log: ModelLog = self.model_log_repository.get_model_log_by_id(feedback_id)

        if model_log.feedback_actual_output is not None:
            raise Exception(f"The feedback has been submitted already")

        response_dto = TextAnalysisFeedbackReviewResponseDTO(
            self.emotion_pic_repository.get_emotion_pic_by_emotion_flag(0),
            self.emotion_pic_repository.get_emotion_pic_by_emotion_flag(1),
            self.emotion_pic_repository.get_emotion_pic_by_emotion_flag(2),
            self.emotion_pic_repository.get_emotion_pic_by_emotion_flag(3),
            self.emotion_pic_repository.get_emotion_pic_by_emotion_flag(4),
            self.emotion_pic_repository.get_emotion_pic_by_emotion_flag(5)
        )

        return response_dto


