from app.redis_client.recommendations import RecommendationsRedisClient
from app.domain.enums import StatusRecommendationsEnum
from app.jobs.recommendations import RecommedationsGetterJob

class RecommendationUpdater:
  def __init__(self, redis_client=RecommendationsRedisClient):
    self.redis_client = redis_client
  
  def call(self, athlete_id):
    self.redis_client().delete(athlete_id)
    self.redis_client().set_status(athlete_id, StatusRecommendationsEnum.PENDING)
    RecommedationsGetterJob.perform_async(athlete_id)
