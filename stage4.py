import requests
import json

def no_prefix():
  r = requests.post('http://challenge.code2040.org/api/prefix', data={'token': '7628d19dc804169849b04c989c364a4e'})
  d = json.loads(r.text)
  print(d['prefix'])
  print(d['array'])
  return [word for word in d['array'] if word[:len(d['prefix'])] != d['prefix']]


if __name__ == '__main__':
  arr = no_prefix()
  clean_arr = json.dumps(arr)
  print(clean_arr)
  print(json.loads(clean_arr))
  s = requests.post('http://challenge.code2040.org/api/prefix/validate', data={'token': '7628d19dc804169849b04c989c364a4e', 'array': clean_arr})
  print(s.status_code)
  print(s.text)
