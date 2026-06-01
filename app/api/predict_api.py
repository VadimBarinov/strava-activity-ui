import httpx
from config import settings

class TypePredictorAPI:
  def __init__(self, url=settings.predictor.url):
    self.url = url
    
  def headers(self):
    return {
      "accept": "application/json",
      "Content-Type": "application/json",
    }
    
  def fetch_predicted_values(self, payload):
    resp = httpx.post(
      self.url,
      headers=self.headers(),
      json=payload,
      timeout=30,
      verify=False,
    )
    resp.raise_for_status()
    return resp.json()["content"]
    
class TypePredictorMapper:
  def payload_for_predict(self, activities_list):
    return {"content": [
      {
        "id": activity.id,
        "average_heartrate": activity.average_heartrate,
        "average_speed": activity.average_speed,
        "distance": activity.distance,
        "moving_time": activity.moving_time,
        "total_elevation_gain": activity.total_elevation_gain,
        "type": activity.type,
      }
      for activity in activities_list
    ]}
