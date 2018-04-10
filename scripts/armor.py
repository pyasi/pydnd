

import requests
import json

dndurl = "http://dnd5eapi.co/api/"
url = "http://127.0.0.1:8000/"
endpoint = 'equipment/'
endpoint2 = 'armor/'

response = requests.get(dndurl + endpoint)
body = response.json()
count = body['count']

for i in range(38, 51):
    try:
        response = requests.get(dndurl + endpoint + str(i))
        if response.ok:
            body = response.json()
            body2={}
            body2["name"]=body["name"]
            body2["desc"]=body["name"]
            body2["armor_category"]=body["armor_category"]
            body2["armor_class"] = body["armor_class"]["base"]
            body2["dex_bonus"]=body["armor_class"]["dex_bonus"]
            body2["armor_bonus"]=body["armor_class"]["max_bonus"]
            body2["weight"]=body["weight"]
            body2["str_min"]=body["str_minimum"]
            body2["stealth_dis"]=body["stealth_disadvantage"]
            body2["cost_quantity"]=body["cost"]["quantity"]
            body2["cost_denom"]=body["cost"]["unit"]
            request = requests.post(url + endpoint2, json=body2)
        print("{}\n".format(i))
    except Exception as e:
        print("Error on: {}".format(i))
        print(e)


    '''name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)
    armor_category = models.ForeignKey(ArmorCategory, on_delete=models.CASCADE, null = True)
    armor_class=models.IntegerField()
    dex_bonus=models.BooleanField()
    armor_bonus=models.IntegerField()
    weight = models.IntegerField()
    str_min=models.IntegerField()
    stealth_dis = models.BooleanField()
    cost_quantity = models.IntegerField()
    cost_denom = models.CharField(max_length=2)'''