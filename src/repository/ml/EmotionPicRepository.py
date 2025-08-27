from sqlalchemy import func
from sqlmodel import select
from model.entity.EmotionPicRepo import EmotionPicRepo
from sqlmodel import Session

from repository.BaseRepository import BaseRepository

class EmotionPicRepository(BaseRepository):

    def get_emotion_pic_by_emotion_flag(self, emotion_flag: int) -> str:
        """Retrieve the CDN URL of an image based on the emotion flag.

        Args:
            emotion_flag (int): The emotion flag to filter by.

        Returns:
            str: The CDN URL of the image corresponding to the emotion flag.

        Upon taken, the data is scrambled and then return the first result.
        """
        import random

        query = select(EmotionPicRepo).where(EmotionPicRepo.emotion == emotion_flag)
        result_set = self.session.exec(query).all()

        random.shuffle(result_set)
        return result_set[0].repository if result_set else None

    def find_all(self):
        return self.session.exec(select(EmotionPicRepo)).all()

    def raw_query(self, query: str):
        return self.session.exec(query).all()