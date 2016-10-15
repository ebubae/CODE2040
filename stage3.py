import requests
import json

def find_needle():
  r = requests.post('http://challenge.code2040.org/api/haystack', data={'token': '7628d19dc804169849b04c989c364a4e'})
  d = json.loads(r.text)
  for idx, val in enumerate(d['haystack']):
    if val == d['needle']:
      return idx

if __name__ == '__main__':
  target = find_needle()
  r = requests.post('http://challenge.code2040.org/api/haystack/validate', data={'token': '7628d19dc804169849b04c989c364a4e', 'needle': target})
