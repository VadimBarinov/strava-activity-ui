from rq import Queue
from redis import Redis
import psycopg2
from contextlib import closing
from config import settings
from app.use_cases.recommendations_generator import RecomendationsGenerator

class RecommedationsGetterJob:
  @classmethod
  def perform_async(cls, user_id):
    redis_conn = Redis.from_url(settings.redis_url)
    queue = Queue(connection=redis_conn)
    queue.enqueue(cls.get_recommendations, user_id, job_timeout=300)
    
  @classmethod
  def get_recommendations(cls, user_id):
    with closing(psycopg2.connect(settings.database_url)) as db_connection:
      RecomendationsGenerator(db_connection).call(user_id)