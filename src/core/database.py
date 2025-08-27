from config.config import settings
from sqlmodel import create_engine, Session



# Database Session Generator

DATABASE_URL = (
    f"mysql+mysqlconnector://{settings.database_user}:{settings.database_password}"
    f"@{settings.database_host}:{settings.database_port}/{settings.database_name}"
)

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session