import json

data = {
    'name':'ACME',
    'shares':100,
    'price' : 542.23
}
json_str = json.dumps(data)
print(data)
print(json_str)