from dataclasses import dataclass
import os
from string import Template

@dataclass
class OpenAIPrompt:
  prompt: str
  system_prompt: str
  
class PromptBuilder:
  def __init__(self):
    self.prompt_folder = self.init_prompt_folder()
    
  def build(self, context):
    full_prompt = self.full_prompt_template().substitute(
      context=context,
    )
    return OpenAIPrompt(prompt=full_prompt, system_prompt=self.system_prompt())
  
  def full_prompt_template(self):
    file_name = "prompt_template.txt"
    with open(self.file_path(file_name), "r", encoding="utf-8") as file:
      return Template(file.read())
    
  def system_prompt(self):
    file_name = "system_prompt.txt"
    with open(self.file_path(file_name), "r", encoding="utf-8") as file:
      return file.read()
    
  def file_path(self, file_name):
    return os.path.join(self.prompt_folder, file_name)
  
  def init_prompt_folder(self):
    current_file_path = os.path.abspath(__file__)
    current_dir_path = os.path.dirname(current_file_path)
    app_path = os.path.dirname(current_dir_path)
    return app_path + "/static/prompts"