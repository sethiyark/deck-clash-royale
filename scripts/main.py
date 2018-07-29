import requests

from config import *

response = requests.get(API_URL + '/clans/' + ' P9QRQ89L', headers=HEADERS).json()

print(response)
