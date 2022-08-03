import json


theFile = "output.json"


with open("output.json", "r", encoding="utf8") as f: # "r" is default
    data = json.load(f)

""" data = [json.loads(line)
        for line in open('output.json', 'r', encoding='utf-8')]

for i in data:
    if i["addressLocality"] == "Örebro":
        print(i) """