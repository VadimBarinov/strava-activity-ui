from flask import render_template, redirect, request, url_for
from flask_login import current_user
from app.use_cases.strava_auth import StravaLoginUrlGetter, StravaLoginUser
from app.use_cases.strava_activities import StravaFetchAllActivities, StravaFetchOneActivity
from .decorators import login_required_with_token
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
  athlete = StravaLoginUser().login_and_get_data(code)
  return redirect(url_for("athlete_activities", athlete.id))

@bp.route("/", methods=["GET"])
def index():
  if current_user:
    redirect(url_for("athlete_activities", current_user.id))
  return render_template("index.html")

@bp.route("/<athlete_id>", methods=["GET"])
@login_required_with_token
def athlete_activities(athlete_id: int):
  activities = StravaFetchAllActivities().call(athlete_id)
  return render_template("athlete_activities.html", activities=activities)

@bp.route("/<athlete_id>/activity/<activity_id>", methods=["GET"])
@login_required_with_token
def activity(athlete_id: int, activity_id: int):
  activity = StravaFetchOneActivity().call(athlete_id, activity_id)
  return render_template("activity.html", activity=activity)