import httpx
from openai import OpenAI
import json
from config import settings

class OpenAIClient:
  def __init__(self):
    http_client = httpx.Client(
      timeout=300,
      verify=False,
    )
    self.client = OpenAI(
      base_url=settings.openrouter.api_base,
      api_key=settings.openrouter.api_key,
      http_client=http_client,
    )
    
  def perform(self, prompt):
    resp = self.client.chat.completions.create(
      model="meta-llama/llama-3.1-8b-instruct",
      messages=[
        {"role": "system", "content": prompt.system_prompt},
        {"role": "user", "content": prompt.prompt},
      ]
    )
    content = resp.choices[0].message.content
    return content