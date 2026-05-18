from functools import wraps
from flask import abort
from flask_login import login_required, logout_user, current_user

def login_required_with_token(view):
  @wraps(view)
  @login_required
  def wrapped(*args, **kwargs):
    # берем access из redis
      # если он не истек, то используем
      # иначе
        # если refress не истек то рефреш
        # иначе logout
    # if ... :
    #   logout_user()
    return view(*args, **kwargs)
  return wrapped