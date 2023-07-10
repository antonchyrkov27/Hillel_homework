import json

file_json = '/Users/kateryna21/Desktop/sample2 2.json'

with open (file_json, 'r') as file:
    data = json.load(file)

print(data)

