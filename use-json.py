import json
from jsonschema import validate


theFile = "output.json"


""" with open("output.json", "r", encoding="utf8") as f: # "r" is default
    data = json.load(f) """


""" data = [json.loads(line)
        for line in open('output.json', 'r', encoding='utf-8')]

for i in data:
    if i["addressLocality"] == "Örebro":
        print(i) """


# Need to format/validate json on read it like this.

""" def validateJsonFile(jsonFile):
    try:
        json.load(jsonFile)
    except ValueError as err:
        print(err)
        return False
    return True


with open(theFile, encoding="utf8") as f:
    print("Json Validated: ", validateJsonFile(f)) """

data = [json.loads(line) for line in open(theFile,'r', encoding="utf8")]

for i in data['originalJobPosting']:
    print(i)

