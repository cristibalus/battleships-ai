from login import login
import requests

url = 'http://ic2020-fea-api.netrom.live/game/'

def shootTest(x, y, token):
  return shoot(x, y, "119", token)

def shoot(x, y, joc, token):
  data = '{"x" : "' + x + '", "y" : "' + y + '"}'
  response = requests.post(url + joc + "/shoot", data=data, headers={"Content-Type": "application/json", "Authorization": 'Bearer ' + token}).json()
  
  return (response["code"])

if __name__ == '__main__':
  token = login()
  print(shootTest("1", "A", token))
  print(shootTest("4", "B", token))
  print(shootTest("5", "D", token))