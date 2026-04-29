from flask import Flask
from config import settings
from .db import database_helper
from .web import bp as web_bp

def create_app():
  app = Flask(__name__)
  app.config["DATABASE_URL"] = settings.database_url
  app.config["SECRET_KEY"] = settings.secret_key
  
  database_helper.init_app(app)
  
  app.register_blueprint(web_bp)

  return app
