from flask import render_template
from . import bp

@bp.route("/", methods=["GET"])
def index():
  # добавить проверку авторизации
  # если пользователь авторизован, то редирект на страницу со списком
  return render_template("index.html")