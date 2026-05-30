from flask import Flask
from config import settings
from .web import bp as web_bp
from .login_manager import login_manager
from .template_filters import convert_date, convert_distance, convert_moving_time, convert_speed

def create_app():
  app = Flask(__name__)
  app.config["DATABASE_URL"] = settings.database_url
  app.config["SECRET_KEY"] = settings.secret_key
  
  login_manager.init_app(app)
  
  app.register_blueprint(web_bp)
  
  app.jinja_env.filters["convert_date"] = convert_date
  app.jinja_env.filters["convert_distance"] = convert_distance
  app.jinja_env.filters["convert_moving_time"] = convert_moving_time
  app.jinja_env.filters["convert_speed"] = convert_speed
  
  from . import db
  db.init_app(app)

  return app
