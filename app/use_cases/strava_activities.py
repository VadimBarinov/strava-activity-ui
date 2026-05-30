from datetime import datetime, timedelta
from app.api.strava_api import StravaAPI
from app.api.predict_api import TypePredictorAPI, TypePredictorMapper
from app.repositories.activities import ActivitiesRepository
from app.redis_client.tokens import TokenRedisClient

class StravaFetchAllActivities:
  def __init__(self, db_connection, strava_api_cls=StravaAPI):
    self.db_connection = db_connection
    self.repository = ActivitiesRepository(db_connection)
    self.strava_api_cls = strava_api_cls
    
  def call(self, athlete_id):
    StravaSyncLastActivities(self.db_connection).call(athlete_id)
    activities = self.repository.fetch_all_by_user_id(athlete_id)
    return activities
  
class StravaSyncLastActivities:
  def __init__(self, db_connection, strava_api_cls=StravaAPI,
               predictor_api_cls=TypePredictorAPI, predictor_mapper_cls=TypePredictorMapper,
               redis_client=TokenRedisClient):
    self.repository = ActivitiesRepository(db_connection)
    self.strava_api_cls = strava_api_cls
    self.predictor_api_cls = predictor_api_cls
    self.predictor_mapper_cls = predictor_mapper_cls
    self.redis_client = redis_client()
  
  def call(self, athlete_id):
    last_start_date = self.repository.fetch_last_start_date_by_user_id(athlete_id)
    token_set = self.redis_client.get(athlete_id)
    
    api = self.strava_api_cls()
    new_activities_from_strava = api.fetch_activities(token_set.access_token, last_start_date)
    
    if new_activities_from_strava:
      for activity_dto in new_activities_from_strava:
        self.repository.save_with_map(activity_dto)
      self.predict_types(new_activities_from_strava)
    
  def predict_types(self, activities):
    api = self.predictor_api_cls()
    mapper = self.predictor_mapper_cls()
    payload = mapper.payload_for_predict(activities)
    activities_response = api.fetch_predicted_values(payload)
    for activity in activities_response:
      self.repository.update_intensity_score_and_target(
        activity["id"], activity["intensity_score"], activity["target"], 
      )
  
class StravaFetchOneActivity:
  def __init__(self, db_connection, strava_api_cls=StravaAPI):
    self.repository = ActivitiesRepository(db_connection)
    self.strava_api_cls = strava_api_cls
    
  def call(self, athlete_id, activity_id):
    activity = self.repository.fetch_by_id_and_user_id(athlete_id, activity_id)
    return activity