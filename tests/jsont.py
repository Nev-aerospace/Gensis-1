import json
from re import X


def JsonTest():
    with open("./config.json") as jsonfile:
        data = json.load(jsonfile)
        x = True

    return X


