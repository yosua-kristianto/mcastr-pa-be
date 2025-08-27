from sqlmodel import select
from model.entity.Config import Config
from sqlmodel import Session

from repository.BaseRepository import BaseRepository

class ConfigRepository(BaseRepository):
    def get_config_by_key(self, key: str) -> str :
        """Get GCO's config value by its key.

        Throws:
            Exception: If config with the given key is not found. 

        Args:
            key (str): The config key to look for.
        
        Returns:
            str: The config's value associated with the given key.
        """

        print(">>>>>>>>>>>> SESSION: ")
        print(self.session)

        result_set = self.session.get(Config, key)

        # Refactor this. Add exception layers
        if result_set is None:
            raise Exception(f"Config with key {key} not found")
        
        return result_set.value
