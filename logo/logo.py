import requests

API = 'https://nidusha-slaptap/logo?name='

req = requests.post(API+input('Name : ').replace(' ','%20'))

print(req.history[1].url)
