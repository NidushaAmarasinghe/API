import requests

API = 'https://nidusha-slaptap/logohq?name='

req = requests.post(API+input('Name : ').replace(' ','%20'))

print(req.history[1].url)
