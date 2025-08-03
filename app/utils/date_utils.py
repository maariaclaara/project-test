from datetime import datetime

def format_brazilian_date(date_obj):
  if isinstance(date_obj, datetime):
      return date_obj.strftime("%d/%m/%Y")
  elif isinstance(date_obj, str):
      try:
          dt = datetime.fromisoformat(date_obj.replace('Z', '+00:00'))
          return dt.strftime("%d/%m/%Y")
      except:
          return date_obj
  return str(date_obj)

def format_brazilian_datetime(date_obj):
  if isinstance(date_obj, datetime):
      return date_obj.strftime("%d/%m/%Y %H:%M")
  elif isinstance(date_obj, str):
      try:
          dt = datetime.fromisoformat(date_obj.replace('Z', '+00:00'))
          return dt.strftime("%d/%m/%Y %H:%M")
      except:
          return date_obj
  return str(date_obj)
