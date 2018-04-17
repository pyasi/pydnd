import requests
import json

dndurl = "http://dnd5eapi.co/api/"
url = "http://127.0.0.1:8000/"
endpoint = 'classes/'
endpoint2 = 'classes/'

response = requests.get(dndurl + endpoint)
body = response.json()
count = body['count']

for i in range(1, int(count) + 1):
    try:
        response = requests.get(dndurl + endpoint + str(i))
        if response.ok:
            body = response.json()
            #print(body['name'])
            #body['desc'] = ''.join(body['desc'])
            request = requests.post(url + endpoint2, json=body)

            if not request.ok and not request.status_code == 400:
                print(body)
        print("{}\n".format(i))
    except Exception as e:
        print("Error on: {}".format(i))
        print(e)
