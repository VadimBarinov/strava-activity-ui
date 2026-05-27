from functools import wraps
from flask_login import login_required, logout_user, current_user
from app.redis_client.tokens import TokenRedisClient
from app.api.strava_api import StravaAPI

def login_required_with_token(view):
  @wraps(view)
  @login_required
  def wrapped(*args, **kwargs):
    redis_client = TokenRedisClient()
    token_set = redis_client.get(current_user.id)
    if token_set.is_expired():
      strava_api = StravaAPI()
      try:
        new_token_set = strava_api.refresh_access_token(
          token_set.refresh_token,
        )
        redis_client.set(new_token_set)
      except Exception:
        logout_user()
    return view(*args, **kwargs)
  return wrapped
