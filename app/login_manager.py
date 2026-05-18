from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "strava_activity.login_strava"
from .web import loaders