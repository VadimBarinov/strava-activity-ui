from config import settings
from redis import Redis

class TokenRedisClient:
  def __init__(self, redis_url=settings.redis_url,
               prefix="oauth:token:"):
    self.connection = Redis.from_url(redis_url, decode_responses=True)
    self.prefix = prefix
  
  def _key(self, key):
    return f"{self.prefix}{key}"
  
  def get(self, key):
    access_token = self.connection.get(self._key(key))
    return access_token
  
  def set(self, token, key, ttl=300):
    obj = {
      "access_token": token.access_token,
      "refresh_token": token.refresh_token,
      "expires_at": int(token.expires_at),
    }
    exat = int(token.expires_at) + ttl
    self.connection.set(self._key(key), obj, exat=exat)