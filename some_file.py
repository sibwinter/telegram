from pprint import pprint
import requests

TOKEN = '5579843922:AAHb9Q1IAAZIUtHHYdlepHh1fuPmqhpmgOA'
METHOD_NAME = 'getMe'
API_URL = f'https://api.telegram.org/bot{TOKEN}/{METHOD_NAME}'

response = requests.get(API_URL)
if response.status_code == 200:
    pprint(response.json())
else:
    print(response.status_code)