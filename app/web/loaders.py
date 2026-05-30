from app.login_manager import login_manager
from app.repositories.users import UsersRepository
from app import db
from app.use_cases.strava_auth import User

@login_manager.user_loader
def load_user(user_id):
  user = UsersRepository(db.get_db()).fetch(user_id)
  if user:
    return User(user.id, user.username, user.firstname, user.lastname)