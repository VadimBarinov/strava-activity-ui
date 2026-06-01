from functools import wraps
from flask_login import login_required, current_user
from app.use_cases.refresh_login import StravaLoginRefresh

def login_required_with_token(view):
  @wraps(view)
  @login_required
  def wrapped(*args, **kwargs):
    StravaLoginRefresh().call(current_user)
    return view(*args, **kwargs)
  return wrapped
