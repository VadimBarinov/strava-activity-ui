from urllib.parse import urlencode
import httpx
from config import settings
from app.domain.dtos import AthleteDto, MapDto, TokenDto, ActivityDto
from datetime import datetime

class StravaAPI:
  def __init__(self, url=settings.strava.api_base):
    self.url = url
    
  def generate_jwt(self, data, token_url=settings.strava.token_url):
    resp = httpx.post(
      token_url,
      data=data,
    )
    resp.raise_for_status()
    token_json = resp.json()
    return TokenDto(
      access_token=token_json["access_token"],
      refresh_token=token_json["refresh_token"],
      expires_at=token_json["expires_at"],
      athlete=AthleteDto(
        id=token_json["athlete"]["id"],
        username=token_json["athlete"]["username"],
        firstname=token_json["athlete"]["firstname"],
        lastname=token_json["athlete"]["lastname"],
      )
    )
    
  def generate_access(self, code, token_url=settings.strava.token_url):
    data = StravaMapper().token_url_data_for_authorization(code)
    return self.generate_jwt(data, token_url)
    
  def refresh_access_token(self, refresh_token, token_url=settings.strava.token_url):
    data = StravaMapper().token_url_data_for_refresh(refresh_token)
    return self.generate_jwt(data, token_url)
  
  def headers(self, access_token):
    return {
      "Authorization": f"Bearer {access_token}",
    }
  
  def fetch_activities(self, access_token, after):
    endpoint_url = self.url + "/athlete/activities"
    if after:
      after_timestamp = int(after.timestamp())
      endpoint_url += f"?after={after_timestamp}"
    resp = httpx.post(
      endpoint_url, 
      headers=self.headers(access_token),
    )
    resp.raise_for_status()
    resp = resp.json()
    return ActivityDto(
      id=resp["id"],
      athlete=AthleteDto(id=resp["athlete"]["id"]),
      name=resp["name"],
      start_date=datetime.fromisoformat(resp["start_date"].replace("Z", "+00:00")),
      type=resp["type"],
      distance=resp["distance"],
      moving_time=resp["moving_time"],
      average_speed=resp["average_speed"],
      max_speed=resp["max_speed"],
      total_elevation_gain=resp["total_elevation_gain"],
      average_heartrate=resp["average_heartrate"],
      max_heartrate=resp["max_heartrate"],
      map=MapDto(
        id=resp["map"]["id"],
        summary_polyline=resp["map"]["summary_polyline"],
      ),
    )
  
class StravaMapper:
  def __init__(self, client_id=settings.strava.client_id):
    self.client_id = client_id
  
  def login_url_params(self, redirect_uri=settings.strava.redirect_uri, 
                scope=settings.strava.scope):
    return {
      "client_id": self.client_id,
      "redirect_uri": redirect_uri,
      "response_type": "code",
      "approval_prompt": "auto",
      "scope": scope,
    }
  
  def login_url(self, url=settings.strava.auth_url, 
                redirect_uri=settings.strava.redirect_uri, 
                scope=settings.strava.scope):
    return f"{url}?{urlencode(self.login_url_params(redirect_uri, scope))}"
    
  def token_url_data_for_authorization(self, code, client_secret=settings.strava.client_secret):
    return {
      "client_id": self.client_id,
      "client_secret": client_secret,
      "code": code,
      "grant_type": "authorization_code",
    }
    
  def token_url_data_for_refresh(self, refresh_token, client_secret=settings.strava.client_secret):
    return {
      "client_id": self.client_id,
      "client_secret": client_secret,
      "grant_type": "refresh_token",
      "refresh_token": refresh_token,
    }
