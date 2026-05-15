from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent
    
class RoutesConfig(BaseModel):
  strava_activity: str = "strava_activity"
  strava_activity_prefix: str = "/strava-activity"
  
class StravaConfig(BaseModel):
  client_id: str
  client_secret: str
  redirect_uri: str
  scope: str
  auth_url: str
  token_url: str
  api_base: str

class Settings(BaseSettings):
  database_url: str
  flask_app: str
  secret_key: str
  redis_url: str
  routes: RoutesConfig = RoutesConfig()
  model_config = SettingsConfigDict(
    env_file=(BASE_DIR / ".env"),
    case_sensitive=False,
    env_nested_delimiter="__",
  )

settings = Settings()