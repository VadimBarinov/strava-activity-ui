from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent
    
class RoutesConfig(BaseModel):
  strava_activity: str = "strava_activity"
  strava_activity_prefix: str = "/strava-activity"

class Settings(BaseSettings):
  flask_app: str
  model_path: str
  routes: RoutesConfig = RoutesConfig()
  model_config = SettingsConfigDict(
    env_file=(BASE_DIR / ".env"),
    case_sensitive=False,
  )

settings = Settings()