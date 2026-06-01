from app.domain.enums import StatusRecommendationsEnum
from app.redis_client.recommendations import RecommendationsRedisClient

class StatusChangeRule:
  def __init__(self):
    self.target_status = StatusRecommendationsEnum.PENDING
    
  def apply(self, redis_client, user_id):
    redis_client.set_status(user_id, self.target_status)
    return self.target_status
  
class MarkPending(StatusChangeRule):
  pass

class MarkDone(StatusChangeRule):
  def __init__(self):
    self.target_status = StatusRecommendationsEnum.DONE
    
class MarkFailure(StatusChangeRule):
  def __init__(self):
    self.target_status = StatusRecommendationsEnum.FAILURE
    
class RecommendationsStatusService:
  def __init__(self, rule=StatusChangeRule(),
               redis_client=RecommendationsRedisClient):
    self._rule = rule
    self.redis_client = redis_client()
    
  def change_status(self, user_id):
    return self._rule.apply(self.redis_client, user_id)
    