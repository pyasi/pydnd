import requests
import json

dndurl = "http://dnd5eapi.co/api/"
url = "http://127.0.0.1:8000/"
endpoint = 'equipment/'
endpoint2 = 'equipment/'

response = requests.get(dndurl + endpoint)
body = response.json()
count = body['count']
body2 = {}

for i in range(51, count):
    try:
        response = requests.get(dndurl + endpoint + str(i))
        if response.ok:
            body = response.json()
            keys = list(body.keys())
            body2["name"]= body["name"]
            body2["desc"]= body["name"]
            body2["equipment_category"]=body[keys[4]]
            body2["cost_quantity"]=body["cost"]["quantity"]
            body2["cost_denom"] = body["cost"]["unit"]

            request = requests.post(url + endpoint2, json=body2)
        print("{}\n".format(i))
    except Exception as e:
        print("Error on: {}".format(i))
        print(e)
