from urllib.parse import urlencode
import httpx
import config
from app.domain.dtos import AthleteDto, TokenDto, ActivityDto

class StravaAPI:
  def __init__(self, url=config.StravaConfig.api_base):
    self.url = url
    
  def generate_jwt(self, payload, token_url=config.StravaConfig.token_url):
    resp = httpx.post(
      token_url,
      json=payload,
      timeout=30,
      verify=False,
    )
    resp.raise_for_status()
    token_json = resp.json()
    print(token_json)
    return TokenDto(
      access_token=token_json["access_token"],
      refresh_token=token_json["refresh_token"],
      expires_at=token_json["expires_at"],
      athlete=AthleteDto(
        id=token_json["athlete"]["id"],
        username=token_json["athlete"]["username"],
      )
    )
    
  def generate_access(self, code, token_url=config.StravaConfig.token_url):
    payload = StravaMapper().token_url_payload_for_authorization(code, token_url)
    return self.generate_jwt(payload)
    
  def refresh_access_token(self, code, token_url=config.StravaConfig.token_url):
    payload = StravaMapper().token_url_payload_for_refresh(code, token_url)
    return self.generate_jwt(payload)
  
  def headers(self, access_token):
    return {
      "Authorization": f"Bearer {access_token}",
    }
    
  def fetch_user_data(self, access_token):
    endpoint_url = self.url + "/athlete"
    resp = httpx.post(
      endpoint_url, 
      headers=self.headers(),
      timeout=30,
      verify=False,
    )
    resp.raise_for_status()
    resp = resp.json()
    print(resp)
    return AthleteDto(
      id=resp["id"],
      username=resp["username"],
      firstname=resp["firstname"],
      lastname=resp["lastname"],
    )
  
  def fetch_activities(self, ):
    # нужно дописать
    endpoint_url = ...
    resp = httpx.post(
      endpoint_url, 
      headers=self.headers(),
      timeout=30,
      verify=False,
    )
    resp.raise_for_status()
    resp = resp.json()
    print(resp)
    return ActivityDto(...)
  
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
  
  def token_url_payload(self, code, grand_type, client_secret=config.StravaConfig.client_secret):
    return {
      "client_id": self.client_id,
      "client_secret": client_secret,
      "code": code,
      "grant_type": grand_type,
    }
    
  def token_url_payload_for_authorization(self, code, client_secret=config.StravaConfig.client_secret):
    return self.token_url_payload(code, "authorization_code", client_secret=client_secret)
    
  def token_url_payload_for_refresh(self, code, client_secret=config.StravaConfig.client_secret):
    return self.token_url_payload(code, "refresh_token", client_secret=client_secret)
    