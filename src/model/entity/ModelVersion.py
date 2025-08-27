from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional

class ModelVersion(SQLModel, table=True):
    __tablename__ = "mlops_tbl_version"

    model_name: str = Field(primary_key=True, max_length=60)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None