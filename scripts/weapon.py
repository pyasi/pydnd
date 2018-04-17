
import requests
import json

dndurl = "http://dnd5eapi.co/api/"
url = "http://127.0.0.1:8000/"
endpoint = 'equipment/'
endpoint2 = 'weapon/'

response = requests.get(dndurl + endpoint)
body = response.json()
count = body['count']

for i in range(1, 38):
    try:
        response = requests.get(dndurl + endpoint + str(i))
        if response.ok:
            body = response.json()
            body2={}
            body2["name"]=body["name"]
            body2["desc"]=body["name"]
            body2["weapon_category"]=body["category_range"]
            body2["range_type"]=body["weapon_range"]
            body2["normal_range"]=body["range"]["normal"]
            body2["long_range"]=body["range"]["long"]
            body2["damage_type"]=body["damage"]["damage_type"]["name"]
            body2["weight"]=body["weight"]
            body2["properties"]=body["properties"]
            try:
                body2["specialproperties"]=body["special"]["0"]
            except KeyError:
                pass
            body2["damage_die_count"]=body["damage"]["dice_count"]
            body2["damage_die"] = body["damage"]["dice_value"]
            body2["cost_quantity"]=body["cost"]["quantity"]
            body2["cost_denom"]=body["cost"]["unit"]
            try:
                body2["normal_throw_range"]=body["throw_range"]["normal"]
                body2["long_throw_range"]=body["throw_range"]["long"]
            except KeyError:
                pass

            request = requests.post(url + endpoint2, json=body2)
            print("{}\n".format(i))
    except Exception as e:
        print("Error on: {}".format(i))
        print(e)
