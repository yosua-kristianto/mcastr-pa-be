from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional

class EmotionPicRepo(SQLModel, table=True):
    __tablename__ = "ml_tbl_emotion_pic_repo"

    uuid: str = Field(primary_key=True)
    emotion: int
    repository: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None