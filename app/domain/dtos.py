from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class AthleteDto:
  id: str
  username: str | None = None
  firstname: str | None = None
  lastname: str | None = None
  
@dataclass
class MapDto:
  id: str
  summary_polyline: str

@dataclass
class TokenDto:
  access_token: str
  refresh_token: str
  expires_at: int
  athlete: AthleteDto
  
  def is_expired(self,
                 now=datetime.now().timestamp(),
                 skew=timedelta(seconds=30).total_seconds()):
    return now + skew >= self.expires_at
  
@dataclass
class ActivityDto:
  id: str
  athlete: AthleteDto
  name: str
  start_date_local: datetime
  type: str
  distance: float
  moving_time: float
  average_speed: float
  max_speed: float
  total_elevation_gain: float
  average_heartrate: float
  max_heartrate: float
  map: MapDto
  intensity_score: float | None = None
  target: float | None = None