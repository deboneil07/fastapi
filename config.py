from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings): # settings class with all env info
    env_name: str = "local"
    base_url: str = "http://localhost:9000"
    db_url : str = "sqlite:///./shortener.db"

class Config:
    env_file = "./.env"

@lru_cache # used for caching
def get_settings() -> Settings:   # get settings returns an object of Settings class
    settings = Settings() # settings is an object of Settings class
    print(f'Loading settings for: {settings.env_name}')
    return settings # returns settings