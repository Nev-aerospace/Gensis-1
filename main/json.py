import json

with open("../config.json") as jsonfile:
    data = json.load(jsonfile)
print(data)
