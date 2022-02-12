import requests

API = 'nidusha-slaptap?write='

req = requests.post(API+input('Text : ').replace(' ','%20'))

print(req.history[1].url)
