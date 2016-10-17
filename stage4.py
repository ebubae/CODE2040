import requests
import json

def no_prefix():
  r = requests.post('http://challenge.code2040.org/api/prefix', data={'token': '7628d19dc804169849b04c989c364a4e'})
  d = json.loads(r.text)
  prefix = d['prefix']
  all_words = d['array']
  print(prefix)
  print(all_words)

  return [word for word in all_words if word[:len(prefix)] != prefix]


if __name__ == '__main__':
  arr = no_prefix()
  clean_arr = json.dumps(arr)
  print(clean_arr)
  s = requests.post('http://challenge.code2040.org/api/prefix/validate', json={'token': '7628d19dc804169849b04c989c364a4e', 'array': no_prefix()})
  print(s.status_code)
  print(s.text)
