from app.redis_client.recommendations import RecommendationsRedisClient
from app.use_cases.status_service import RecommendationsStatusService, MarkPending
from app.jobs.recommendations import RecommedationsGetterJob

class RecommendationUpdater:
  def __init__(self, redis_client=RecommendationsRedisClient):
    self.redis_client = redis_client
  
  def call(self, athlete_id):
    self.redis_client().delete(athlete_id)
    RecommendationsStatusService(MarkPending()).change_status(athlete_id)
    RecommedationsGetterJob.perform_async(athlete_id)
