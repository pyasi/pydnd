import requests
import json

url = "http://127.0.0.1:8000/"

with open('scripts/monsters.json', 'r') as file:
    datastore = json.load(file)
    for obj in datastore:
        try:
            response = requests.post(url + "monsters", json=obj)
            if response.status_code == 500:
                print(response)
        except Exception as e:
            print(e)
            print(obj)



