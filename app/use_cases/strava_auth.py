from flask_login import login_user, UserMixin
from app.api.strava_api import StravaAPI, StravaMapper
from app.redis_client.tokens import TokenRedisClient
from app.repositories.users import UsersRepository

class User(UserMixin):
  def __init__(self, user_id, username, firstname, lastname):
    self.id = user_id
    self.username = username
    self.firstname = firstname
    self.lastname = lastname

class StravaLoginUrlGetter:
  def __init__(self, strava_mapper_cls=StravaMapper):
    self.strava_mapper_cls = strava_mapper_cls
    
  def call(self):
    mapper = StravaMapper()
    return mapper.login_url()
  
class StravaLoginUser:
  def __init__(self, db_connection, strava_api_cls=StravaAPI, user_cls=User,
               redis_client=TokenRedisClient):
    self.repository = UsersRepository(db_connection)
    self.strava_api_cls = strava_api_cls
    self.user_cls = user_cls
    self.redis_client = redis_client()
  
  def call(self, code):
    api = self.strava_api_cls()
    token_set = api.generate_access(code)
    self.redis_client.set(token_set)
    
    user_record = self.repository.fetch(token_set.athlete.id)
    if not user_record:
      self.repository.save(token_set.athlete)
      
    user = self.user_cls(
      user_id=token_set.athlete.id,
      username=token_set.athlete.username,
      firstname=token_set.athlete.firstname,
      lastname=token_set.athlete.lastname,
    )
    login_user(user, remember=True)