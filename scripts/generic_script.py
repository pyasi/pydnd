import requests
import json

dndurl = "http://dnd5eapi.co/api/"
url = "http://127.0.0.1:8000/"
endpoint = 'damage-types/'
endpoint2 = 'damagetypes/'

response = requests.get(dndurl + endpoint)
body = response.json()
count = body['count']

for i in range(1, int(count)):
    try:
        response = requests.get(dndurl + endpoint + str(i))
        if response.ok:
            body = response.json()
            body['desc'] = ''.join(body['desc'])
            request = requests.post(url + endpoint2, json=body)
        print("{}\n".format(i))
    except Exception as e:
        print("Error on: {}".format(i))
        print(e)
