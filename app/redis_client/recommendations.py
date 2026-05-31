from config import settings
from redis import Redis

class RecommendationsRedisClient:
  def __init__(self, redis_url=settings.redis_url,
               prefix="recommendations:"):
    self.connection = Redis.from_url(redis_url, decode_responses=True)
    self.prefix = prefix
  
  def _key(self, key):
    return f"{self.prefix}{key}"
  
  def _key_status(self, key):
    return f"{self.prefix}status:{key}"
  
  def get(self, key):
    return self.connection.get(self._key(key))
  
  def set(self, key, recommendations):
    self.connection.set(self._key(key), recommendations)
    
  def get_status(self, key):
    return self.connection.get(self._key_status(key))
    
  def set_status(self, key, status):
    self.connection.set(self._key_status(key), status.value)
    
  def delete(self, key):
    self.connection.delete(self._key(key))