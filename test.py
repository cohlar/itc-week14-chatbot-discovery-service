import requests


url = 'http://127.0.0.1:5000/'
api = 'api/discovery'
endpoint = {'endpoint': 'dsgfrrgr'}


x = requests.post(url + api, json=endpoint)
print(x.text)
