from model.entity import ModelLog
from sqlmodel import Session, select
from datetime import datetime

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

    def get_model_log_by_id(self, id: str) -> ModelLog:
        """Get model log by its uuid."""

        result_set = self.session.get(ModelLog, id)

        if result_set is None:
            raise Exception(f"Log with id of {id} is not found")

        return result_set

    def update_model_log_actual_output(self, id: str, review: int):
        """Update model log actual output
        """

        result_set = self.session.get(ModelLog, id)

        if result_set is None:
            raise Exception(f"Log with id of {id} is not found")

        result_set.feedback_actual_output = review
        result_set.updated_at = datetime.now()
        self.session.add(result_set)
        self.session.commit()

