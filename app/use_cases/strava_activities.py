from datetime import datetime, timedelta
from app.api.strava_api import StravaAPI
from app.repositories.activities import ActivitiesRepository
from app.redis_client.tokens import TokenRedisClient

def convert_date(iso_date: str):
  dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
  return dt.strftime("%d %B %Y г. в %H:%M")

def convert_distance(distance_in_metres):
  return distance_in_metres / 1000

def convert_moving_time(seconds):
  delta = timedelta(seconds=seconds)
  return str(delta)

def convert_speed(speed):
  return speed * 3.6

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
               redis_client=TokenRedisClient):
    self.repository = ActivitiesRepository(db_connection)
    self.strava_api_cls = strava_api_cls
    self.redis_client = redis_client()
  
  def call(self, athlete_id):
    last_start_date = self.repository.fetch_last_start_date_by_user_id(athlete_id)
    token_set = self.redis_client.get(athlete_id)
    
    api = self.strava_api_cls()
    new_activities_from_strava = api.fetch_activities(token_set.access_token, last_start_date)
    for activity_dto in new_activities_from_strava:
      self.repository.save_with_map(activity_dto)
      
    self.predict_types()
    
  def predict_types(self):
    # отправляет запрос на api для классификации
    # обновляет записи в бд (добавляет target и intensity_score)
    pass
  
class StravaFetchOneActivity:
  def __init__(self, db_connection, strava_api_cls=StravaAPI):
    self.repository = ActivitiesRepository(db_connection)
    self.strava_api_cls = strava_api_cls
    
  def call(self, athlete_id, activity_id):
    activity = self.repository.fetch_by_id_and_user_id(athlete_id, activity_id)
    return activity