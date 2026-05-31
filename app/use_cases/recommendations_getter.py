from app.redis_client.recommendations import RecommendationsRedisClient
from app.domain.enums import StatusRecommendationsEnum
    
class RecommendationsGetter:
  def __init__(self, redis_client=RecommendationsRedisClient):
    self.redis_client = redis_client
    
  def get_recommendations(self, athlete_id):
    return self.redis_client().get(athlete_id)
  
  def get_status(self, athlete_id):
    status = self.redis_client().get_status(athlete_id)
    if status:
      return StatusRecommendationsEnum(status)