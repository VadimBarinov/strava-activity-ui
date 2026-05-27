from config import settings
from redis import Redis
from app.domain.dtos import TokenDto, AthleteDto
import json

class TokenRedisClient:
  def __init__(self, redis_url=settings.redis_url,
               prefix="oauth:token:"):
    self.connection = Redis.from_url(redis_url, decode_responses=True)
    self.prefix = prefix
  
  def _key(self, key):
    return f"{self.prefix}{key}"
  
  def get(self, key):
    str_obj = self.connection.get(self._key(key))
    obj = json.loads(str_obj)
    token_set = TokenDto(
      access_token=obj["access_token"],
      refresh_token=obj["refresh_token"],
      expires_at=obj["expires_at"],
      athlete=AthleteDto(
        id=obj["athlete_id"],
        username=obj["athlete_username"],
        firstname=obj["athlete_firstname"],
        lastname=obj["athlete_lastname"],
      )
    )
    return token_set
  
  def set(self, token):
    obj = {
      "access_token": token.access_token,
      "refresh_token": token.refresh_token,
      "expires_at": int(token.expires_at),
      "athlete_id": token.athlete.id,
      "athlete_username": token.athlete.username,
      "athlete_firstname": token.athlete.firstname,
      "athlete_lastname": token.athlete.lastname,
    }
    str_obj = json.dumps(obj)
    self.connection.set(self._key(token.athlete.id), str_obj)