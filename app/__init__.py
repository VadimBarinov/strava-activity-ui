from flask import Flask
from config import settings
from .db import database_helper
from .web import bp as web_bp
from .login_manager import login_manager

def create_app():
  app = Flask(__name__)
  app.config["DATABASE_URL"] = settings.database_url
  app.config["SECRET_KEY"] = settings.secret_key
  
  database_helper.init_app(app)
  
  login_manager.init_app(app)
  
  app.register_blueprint(web_bp)

  return app
