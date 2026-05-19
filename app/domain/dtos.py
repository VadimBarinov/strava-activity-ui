from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class AthleteDto:
  id: int
  username: str
  firstname: str
  lastname: str

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
  pass