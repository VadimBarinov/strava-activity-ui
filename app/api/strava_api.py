from urllib.parse import urlencode
import httpx
import config
from dataclasses import dataclass
  
@dataclass
class AthleteSet:
  id: int
  username: str
  
@dataclass
class TokenSet:
  access_token: str
  refresh_token: str
  expires_at: int
  athlete: AthleteSet

class StravaAPI:
  def __init__(self, url=config.StravaConfig.api_base):
    self.url = url
    
  def generate_jwt(self, code, token_url=config.StravaConfig.token_url):
    data = StravaMapper().token_url_data(code)
    resp = httpx.post(token_url, data=data)
    resp.raise_for_status()
    token_json = resp.json()
    return TokenSet(
      access_token=token_json["access_token"],
      refresh_token=token_json["refresh_token"],
      expires_at=token_json["expires_at"],
      athlete=AthleteSet(
        id=token_json["athlete"]["id"],
        username=token_json["athlete"]["username"],
      )
    )
  
  def fetch_activities(self, ):
    pass
  
class StravaMapper:
  def __init__(self, client_id=config.StravaConfig.client_id):
    self.client_id = client_id
  
  def login_url_params(self, redirect_uri=config.StravaConfig.redirect_uri, 
                scope=config.StravaConfig.scope):
    return {
      "client_id": self.client_id,
      "redirect_uri": redirect_uri,
      "response_type": "code",
      "approval_prompt": "auto",
      "scope": scope,
    }
  
  def login_url(self, url=config.StravaConfig.auth_url, 
                redirect_uri=config.StravaConfig.redirect_uri, 
                scope=config.StravaConfig.scope):
    return f"{url}?{urlencode(self.login_url_params(redirect_uri, scope))}"
  
  def token_url_data(self, code, client_secret=config.StravaConfig.client_secret):
    return {
      "client_id": self.client_id,
      "client_secret": client_secret,
      "code": code,
      "grant_type": "authorization_code",
    }