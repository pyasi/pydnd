import requests
import json

dndurl = "http://dnd5eapi.co/api/"
url = "http://127.0.0.1:8000/"
endpoint = 'equipment/'
endpoint2 = 'equipment_subcategory/'

response = requests.get(dndurl + endpoint)
body = response.json()
count = body['count']
body2 = {}

for i in range(51, 52):
    try:
        response = requests.get(dndurl + endpoint + str(i))
        if response.ok:
            body = response.json()
            keys = list(body.keys())
            body2["name"]= body[keys[4]]
            body2["desc"]=body[keys[4]]
            body2["equipment_category"]=body[keys[3]]

            request = requests.post(url + endpoint2, json=body)
        print("{}\n".format(i))
    except Exception as e:
        print("Error on: {}".format(i))
        print(e)
