from app.repositories.activities import ActivitiesRepository
from app.redis_client.recommendations import RecommendationsRedisClient
from app.domain.prompt_builder import PromptBuilder
from app.domain.enums import StatusRecommendationsEnum
from app.api.openai import OpenAIClient
import json
from dataclasses import asdict

class RecomendationsGenerator:
  def __init__(self, db_connection, redis_client=RecommendationsRedisClient):
    self.repository = ActivitiesRepository(db_connection)
    self.redis_client = redis_client
    
  def call(self, athlete_id):
    activities = self.repository.fetch_all_by_user_id(athlete_id)[:10]
    recommendations = self.request_from_ai(activities)
    self.redis_client().set(athlete_id, recommendations)
    self.redis_client().set_status(athlete_id, StatusRecommendationsEnum.DONE)
    
  def request_from_ai(self, activities):
    json_data = [
      json.dumps(asdict(activity), default=str)
      for activity in activities
    ]
    prompt = PromptBuilder().build(json_data)
    return OpenAIClient().perform(prompt)
