import requests


url = 'https://chatbot-discovery.herokuapp.com/'
api = 'api/discovery'
endpoint = {'endpoint': 'ENTER YOUR ENDPOINT URL HERE'}


post = requests.post(url + api, json=endpoint)
print(post.text)


get = requests.get(url + api)
print(get.text)


delete = requests.delete(url + api, json=endpoint)
print(delete.text)