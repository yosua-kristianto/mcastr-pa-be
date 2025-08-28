from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional

class Config(SQLModel, table=True):
    __tablename__ = "gco_tbl_config"

    key: str = Field(primary_key=True, max_length=60)
    value: str
    data_type: str = Field(max_length=20)

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None