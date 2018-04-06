import requests
import json

url = "http://127.0.0.1:8000/"

mechanics = ['languages', 'damage_vulnerabilities', 'damage_resistances', 'damage_immunities', 'condition_immunities']

failures = []

with open('scripts/monsters.json', 'r') as file:
    datastore = json.load(file)
    for obj in datastore:
        try:
            for mechanic in mechanics:
                if len(obj[mechanic]) > 1:
                    obj[mechanic] = obj[mechanic].split(', ')
            response = requests.post(url + "monsters/", json=obj)
            if response.status_code == 500:
                print(response)
                failures.append(obj['index'])
            if response.status_code == 404:
                print(obj['index'])
                failures.append(obj['index'])
        except Exception as e:
            print(e)
            print(obj)
            failures.append(obj['index'])
print('Failures: {}'.format(failures))