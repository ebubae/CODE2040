import requests
import json
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

if __name__ == '__main__':
  r = requests.post('http://challenge.code2040.org/api/dating', json={'token': '7628d19dc804169849b04c989c364a4e'})
  data = json.loads(r.text)
  print("interval: ", data['interval'])
  start = parse(data['datestamp'])
  print(data['datestamp'])
  print(start.isoformat())
  delta = relativedelta(seconds=+int(data['interval']))
  stamp = (start + delta).isoformat().replace('+00:00', 'Z')
  print(delta)
  print(stamp)
  s = requests.post('http://challenge.code2040.org/api/dating/validate', json={'token': '7628d19dc804169849b04c989c364a4e', 'datestamp': stamp})
  print(s.status_code)
  print(s.text)
