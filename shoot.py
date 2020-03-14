from login import login
import requests

urlTest = 'http://ic2020-fea-api.netrom.live/game/119/shoot'

def shootTest(x, y, token):
  data = '{"x" : "' + x + '", "y" : "' + y + '"}'

  response = requests.post(urlTest, data=data, headers={"Content-Type": "application/json", "Authorization": 'Bearer ' + token}).json()

  return (response["code"])

if __name__ == '__main__':
  token = login()
  print(shootTest("1", "A", token))
  print(shootTest("4", "B", token))
  print(shootTest("5", "D", token))