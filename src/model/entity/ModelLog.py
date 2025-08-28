from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional

class ModelLog(SQLModel, table=True):
    __tablename__ = "mlops_tbl_model_log"

    uuid: str = Field(primary_key=True)
    version_id: str = Field(foreign_key="mlops_tbl_version.model_name")
    user_session_id: str
    prompt: str
    model_output: int
    feedback_actual_output: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None