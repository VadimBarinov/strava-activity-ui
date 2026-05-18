from flask_login import login_user, UserMixin
from app.api.strava_api import StravaAPI, StravaMapper

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
  def __init__(self, strava_api_cls=StravaAPI, user_cls=User):
    self.strava_api_cls = strava_api_cls
    self.user_cls = user_cls
  
  def login_and_get_data(self, code):
    api = self.strava_api_cls()
    token_set = api.generate_access(code)
    # сохранение токена в redis
    athlete = api.fetch_user_data(access_token=token_set.access_token)
    # здесь еще должна быть проверка на существование пользователя в бд
      # если его нет, то добавляем
    user = self.user_cls(
      user_id=athlete.id,
      username=athlete.username,
      firstname=athlete.firstname,
      lastname=athlete.lastname,
    )
    login_user(user, remember=True)
    return athlete