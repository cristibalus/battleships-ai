import requests

urlLogin = 'http://ic2020-fea-api.netrom.live/login_check'

def login():
  data = '''{
  "username" : "the-fearless-meerkats",
  "password" : "KGnz9s2wDhqe3GZH"
  }
  '''

  return requests.post(urlLogin, data=data, headers={"Content-Type": "application/json"}).json()["token"]
