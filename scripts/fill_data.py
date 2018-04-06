import requests
import json

url = "http://127.0.0.1:8000/"

failures = []

with open('scripts/monsters.json', 'r') as file:
    datastore = json.load(file)
    for obj in datastore:
        try:
            obj['languages'] = obj['languages'].split(', ')
            obj['damage_vulnerabilities'] = obj['damage_vulnerabilities'].split(', ')
            obj['damage_resistances'] = obj['damage_resistances'].split(', ')
            obj['damage_immunities'] = obj['damage_immunities'].split(', ')
            obj['condition_immunities'] = obj['condition_immunities'].split(', ')
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