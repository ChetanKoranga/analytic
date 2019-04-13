import json

with open('today.json','r') as today:
    json_data = [json.loads(line) for line in today]

source = json.dumps(json_data,indent=2)

today_data = json.loads(source)


