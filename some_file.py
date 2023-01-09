import requests

API_URL = 'http://api.open-notify.org/iss-now.json'

response = requests.get(API_URL)
if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)