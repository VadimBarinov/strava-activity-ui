from datetime import timedelta

def convert_date(date: str):
  if not date:
    return None
  return date.strftime("%d %B %Y г. в %H:%M")

def convert_distance(distance_in_metres):
  if not distance_in_metres:
    return None
  return distance_in_metres / 1000

def convert_moving_time(seconds):
  if not seconds:
    return None
  return str(timedelta(seconds=seconds))

def convert_speed(speed):
  if not speed:
    return None
  return speed * 3.6