import requests

def rev_string():
  r = requests.post('http://challenge.code2040.org/api/reverse', data={'token': '7628d19dc804169849b04c989c364a4e'})
  print(r.text)
  rev = r.text[::-1]
  print(rev)
  s = requests.post('http://challenge.code2040.org/api/reverse/validate', data={'token': '7628d19dc804169849b04c989c364a4e', 'string': rev})

if __name__ == '__main__':
  rev_string()
