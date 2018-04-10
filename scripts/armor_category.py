
import requests
import json

dndurl = "http://dnd5eapi.co/api/"
url = "http://127.0.0.1:8000/"
endpoint = 'equipment/'
endpoint2 = 'armor_category/'

response = requests.get(dndurl + endpoint)
body = response.json()
count = body['count']

for i in range(38, 51):
    try:
        response = requests.get(dndurl + endpoint + str(i))
        if response.ok:
            body = response.json()
            body2={}
            body2["name"]=body["armor_category"]
            request = requests.post(url + endpoint2, json=body2)
            print("{}\n".format(i))
    except Exception as e:
        print("Error on: {}".format(i))
        print(e)
