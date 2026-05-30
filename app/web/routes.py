from flask import render_template, redirect, request, url_for
from flask_login import current_user, logout_user
from app.use_cases.strava_auth import StravaLoginUrlGetter, StravaLoginUser
from app.use_cases.strava_activities import StravaFetchAllActivities, StravaFetchOneActivity, StravaSyncLastActivities
from .decorators import login_required_with_token
from app import db
from . import bp

@bp.route("/login/strava", methods=["GET"])
def login_strava():
  return redirect(StravaLoginUrlGetter().call())

@bp.route("/strava/callback", methods=["GET"])
def strava_callback():
  error = request.args.get("error")
  if error:
    return f"Strava error: {error}", 400
  code = request.args.get("code")
  if not code:
    return "No code returned", 400
  StravaLoginUser(db.get_db()).call(code)
  return redirect(url_for("strava_activity.athlete_activities"))

@bp.route("/logout/strava", methods=["GET"])
def logout_strava():
  logout_user()
  return redirect(url_for("strava_activity.index"))

@bp.route("/", methods=["GET"])
def index():
  if current_user.is_authenticated:
    return redirect(url_for("strava_activity.athlete_activities"))
  return render_template("index.html")

@bp.route("/athlete-activities", methods=["GET"])
@login_required_with_token
def athlete_activities():
  activities = StravaFetchAllActivities(db.get_db()).call(current_user.id)
  return render_template("athlete_activities.html", activities=activities)

@bp.route("/activity/<activity_id>", methods=["GET"])
@login_required_with_token
def activity(activity_id: int):
  activity = StravaFetchOneActivity(db.get_db()).call(current_user.id, activity_id)
  return render_template("activity.html", activity=activity)