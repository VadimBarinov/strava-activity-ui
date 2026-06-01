from flask_login import logout_user
from app.api.strava_api import StravaAPI
from app.redis_client.tokens import TokenRedisClient
from app.domain.dtos import AthleteDto

class StravaLoginRefresh:
  def __init__(self, strava_api_cls=StravaAPI, redis_client=TokenRedisClient):
    self.strava_api_cls = strava_api_cls
    self.redis_client = redis_client()
    
  def call(self, user):
    token_set = self.redis_client.get(user.id)
    if token_set.is_expired():
      strava_api = self.strava_api_cls()
      try:
        new_token_set = strava_api.refresh_access_token(
          token_set.refresh_token,
        )
        new_token_set.athlete = AthleteDto(
          id=user.id,
          username=user.username,
          firstname=user.firstname,
          lastname=user.lastname,
        )
        self.redis_client.set(new_token_set)
      except Exception:
        logout_user()