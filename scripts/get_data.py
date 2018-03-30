import requests
import json

dndurl = "http://dnd5eapi.co/api/"

url = "http://127.0.0.1:8000"

response = requests.get(dndurl + "monsters/")
body = response.json()
count = body['count']

attributes = set()

with open('monsters.json', 'w') as file:

    for i in range(1, int(count)):
        try:
            response = requests.get(dndurl + "monsters/" + str(i))
            body = response.json()
            for key in body:
                attributes.add(key)
            body.pop('url')
            json.dump(body, file)
            file.write(',\n')
            print("{}\n".format(i))
        except Exception as e:
            print("Error on: {}".format(i))
            print(e)
print(attributes)
file.close()
