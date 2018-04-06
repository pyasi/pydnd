import requests
import json

dndurl = "http://dnd5eapi.co/api/"
url = "http://127.0.0.1:8000/"
endpoint = 'equipment/'
endpoint2 = 'equipment_category/'

response = requests.get(dndurl + endpoint)
body = response.json()
count = body['count']


for i in range(51, count):
    try:
        response = requests.get(dndurl + endpoint + str(i))
        if response.ok:
            body = response.json()
            keys = list(body.keys())
            category = body[keys[3]]
            sub_category = body[keys[4]]
            body["name"]=body[keys[3]]
            body["desc"]=body[keys[3]]
            request = requests.post(url + endpoint2, json=body)
        print("{}\n".format(i))
    except Exception as e:
        print("Error on: {}".format(i))
        print(e)