from flask import Blueprint
from config import settings

bp = Blueprint(settings.routes.strava_activity, __name__,
               url_prefix=settings.routes.strava_activity_prefix)
from . import routes
