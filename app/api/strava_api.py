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
      timeout=30,
      verify=False,
    )
    resp.raise_for_status()
    token_json = resp.json()
    return TokenDto(
      access_token=token_json["access_token"],
      refresh_token=token_json["refresh_token"],
      expires_at=token_json["expires_at"],
      athlete=AthleteDto(
        id=str(token_json["athlete"]["id"]),
        username=token_json["athlete"]["username"],
        firstname=token_json["athlete"]["firstname"],
        lastname=token_json["athlete"]["lastname"],
      )
    )
    
  def refresh_jwt(self, data, token_url=settings.strava.token_url):
    resp = httpx.post(
      token_url,
      data=data,
      timeout=30,
      verify=False,
    )
    resp.raise_for_status()
    token_json = resp.json()
    return TokenDto(
      access_token=token_json["access_token"],
      refresh_token=token_json["refresh_token"],
      expires_at=token_json["expires_at"],
    )
    
  def generate_access(self, code, token_url=settings.strava.token_url):
    data = StravaMapper().token_url_data_for_authorization(code)
    return self.generate_jwt(data, token_url)
    
  def refresh_access_token(self, refresh_token, token_url=settings.strava.token_url):
    data = StravaMapper().token_url_data_for_refresh(refresh_token)
    return self.refresh_jwt(data, token_url)
  
  def headers(self, access_token):
    return {
      "Authorization": f"Bearer {access_token}",
    }
  
  def fetch_activities(self, access_token, after):
    endpoint_url = self.url + "/athlete/activities?per_page=100"
    if after:
      after_timestamp = int(after.timestamp())
      endpoint_url += f"&after={after_timestamp}"
    resp = httpx.get(
      endpoint_url, 
      headers=self.headers(access_token),
      timeout=30,
      verify=False,
    )
    resp.raise_for_status()
    resp = resp.json()
    return [
      ActivityDto(
        id=str(activity["id"]),
        athlete=AthleteDto(id=str(activity["athlete"]["id"])),
        name=activity["name"],
        start_date=datetime.fromisoformat(activity["start_date"].replace("Z", "+00:00")),
        start_date_local=datetime.fromisoformat(activity["start_date_local"].replace("Z", "+00:00")),
        type=activity["type"],
        distance=activity["distance"],
        moving_time=activity["moving_time"],
        average_speed=activity["average_speed"],
        max_speed=activity["max_speed"],
        total_elevation_gain=activity["total_elevation_gain"],
        average_heartrate=activity["average_heartrate"],
        max_heartrate=activity["max_heartrate"],
        map=MapDto(
          id=str(activity["map"]["id"]),
          summary_polyline=activity["map"]["summary_polyline"],
        ),
      )
      for activity in resp
    ]
  
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
