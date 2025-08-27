from abc import ABC

class BaseRepository(ABC):

    def __init__(self, session):
        self.session = session