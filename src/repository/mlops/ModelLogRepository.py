from model.entity import ModelLog
from sqlmodel import Session

from repository import BaseRepository

class ModelLogRepository(BaseRepository):
    def create_model_log(self, obj: ModelLog):
        """Create a new model log entry to the database.

        Args:
            obj (ModelLog): The ModelLog object to be created.
        """

        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
