import json

data = [
    {
        'name': 'John',
        'age': 34
    },
    {
        'name': 'Oksana',
        'age': 36
    }
]

data_s = json.dumps(data, indent=4)
# print(type(data_s))
# print(data_s)

recovered_data_from_string = json.loads(data_s)
print(recovered_data_from_string)

with open('json_data.json', 'w') as f:
    json.dump(data, f, indent=4)

with open('json_data.json', 'r') as f:
    json_obj = json.load(f)

# print(json_obj[1]['name'])
