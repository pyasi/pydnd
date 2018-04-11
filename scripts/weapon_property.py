
import requests
import json

dndurl = "http://dnd5eapi.co/api/"
url = "http://127.0.0.1:8000/"
endpoint = 'weapon-properties/'
endpoint2 = 'weapon_property/'

response = requests.get(dndurl + endpoint)
body = response.json()
count = body['count']

for i in range(1, count+1):
    try:
        response = requests.get(dndurl + endpoint + str(i))
        if response.ok:
            body = response.json()
            desc=''
            desc_dict = body.pop("desc")
            for result in desc_dict:
                desc = desc + str(result)
            body["desc"]=desc
            request = requests.post(url + endpoint2, json=body)
            print("{}\n".format(i))
    except Exception as e:
        print("Error on: {}".format(i))
        print(e)
