import requests
import json

dndurl = "http://dnd5eapi.co/api/"
endpoint = 'subclasses/'

response = requests.get(dndurl + endpoint)
body = response.json()
count = body['count']

attribute_set = set()

for i in range(1, int(count)):
    try:
        response = requests.get(dndurl + endpoint + str(i))
        if response.ok:
            body = response.json()
            for key in body:
                attribute_set.add(key)
        print("{}\n".format(i))
    except Exception as e:
        print("Error on: {}".format(i))
        print(e)

print(attribute_set)