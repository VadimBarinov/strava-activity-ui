from flask import render_template
from datetime import datetime, timedelta
from . import bp

def convert_date(iso_date: str):
  dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
  return dt.strftime("%d %B %Y г. в %H:%M")

def convert_distance(distance_in_metres):
  return distance_in_metres / 1000

def convert_moving_time(seconds):
  delta = timedelta(seconds=seconds)
  return str(delta)

def convert_speed(speed):
  return speed * 3.6

@bp.route("/", methods=["GET"])
def index():
  # добавить проверку авторизации
  # если пользователь авторизован, то редирект на страницу со списком
  return render_template("index.html")

@bp.route("/<athlete_id>", methods=["GET"])
def athlete_activities(athlete_id: int):
  # добавить проверку
  # только пользователь с таким id может перейти к своим тренировкам
  
  # получать тренировки из базы
  
  # еще на странице должна быть кнопка синхронизации (тянет данные со strava api и подсчитывает target)
  # это будет асинхронная джоба
  # так же ее запускать при каждом заходе на страницу (не забываем про ограничения по запросам в strava api)
  activities = [
    {
      "athlete": {
        "id": 123,
        "name": "Вадим Баринов",
      },
      "id": 16094685299,
      "name": "Тренировка (после обеда)",
      "start_date_local": convert_date("2025-09-22T17:54:39Z"),
      "type": "Ride",
      "distance":convert_distance(3000),
      "moving_time": convert_moving_time(100),
      "average_speed": convert_speed(6.7), 
      "total_elevation_gain": 300, 
      "average_heartrate": 140,
      "intensity_score": 0.57,
      "target": 2,
    },
    {
      "athlete": {
        "id": 123,
        "name": "Вадим Баринов",
      },
      "id": 16094685299,
      "name": "Тренировка (после обеда)",
      "start_date_local": convert_date("2025-09-22T17:54:39Z"),
      "type": "Run",
      "distance":convert_distance(3000),
      "moving_time": convert_moving_time(100),
      "average_speed": convert_speed(6.7), 
      "total_elevation_gain": 300, 
      "average_heartrate": 140,
      "intensity_score": 0.57,
      "target": 2,
    }
  ]
  return render_template("athlete_activities.html", activities=activities)

@bp.route("/<athlete_id>/activity/<activity_id>", methods=["GET"])
def activity(athlete_id: int, activity_id: int):
  # добавить проверку(сделать декоратор)
  # только пользователь с таким id может перейти к своим тренировкам
  
  # получать данные из базы по конкретной тренировке 
  
  # так же добавить кнопку синхронизации 
  activity = {
    "athlete": {
      "id": 123,
      "name": "Вадим Баринов",
    },
    "id": 16094685299,
    "name": "Тренировка (после обеда)",
    "start_date_local": convert_date("2025-09-22T17:54:39Z"),
    "type": "Ride",
    "distance":convert_distance(3000),
    "moving_time": convert_moving_time(100),
    "average_speed": convert_speed(6.7), 
    "total_elevation_gain": 300, 
    "average_heartrate": 140,
    "intensity_score": 0.57,
    "target": 2,
  }
  return render_template("athlete_activities.html", activity=activity)

# возможно нужно будет добавить эндпоинт login для редиректа со strava