from flask import render_template
from . import bp

@bp.route("/", methods=["GET"])
def index():
  # добавить проверку авторизации
  # если пользователь авторизован, то редирект на страницу со списком
  return render_template("index.html")

@bp.route("/<athlete_id>", methods=["GET"])
def athlete_activities():
  # добавить проверку
  # только пользователь с таким id может перейти к своим тренировкам
  
  # получать тренировки из базы
  
  # еще на странице должна быть кнопка синхронизации (тянет данные со strava api и подсчитывает target)
  # это будет асинхронная джоба
  # так же ее запускать при каждом заходе на страницу (не забываем про ограничения по запросам в strava api)
  activities = None
  return render_template("athlete_activities.html", activities=activities)

@bp.route("/<athlete_id>/activity/", methods=["GET"])
def activity():
  # добавить проверку(сделать декоратор)
  # только пользователь с таким id может перейти к своим тренировкам
  
  # получать данные из базы по конкретной тренировке 
  
  # так же добавить кнопку синхронизации 
  activity = None
  return render_template("athlete_activities.html", activity=activity)

# возможно нужно будет добавить эндпоинт login для редиректа со strava