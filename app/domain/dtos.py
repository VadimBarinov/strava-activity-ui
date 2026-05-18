from dataclasses import dataclass

@dataclass
class AthleteDto:
  id: int
  username: str
  firstname: str|None = None
  lastname: str|None = None

@dataclass
class TokenDto:
  access_token: str
  refresh_token: str
  expires_at: int
  athlete: AthleteDto
  
@dataclass
class ActivityDto:
  pass