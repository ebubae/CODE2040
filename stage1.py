import requests

def make_request():
  '''
  Check the request went well.

  >>> r = make_request()
  >>> r.status_code
  200
  >>> r.text
  'Step 1 complete'
  '''

  r = requests.post('http://challenge.code2040.org/api/register', data={'token': '7628d19dc804169849b04c989c364a4e', 'github': 'https://github.com/ebubae/CODE2040'})
  return r

if __name__ == '__main__':
  make_request()
