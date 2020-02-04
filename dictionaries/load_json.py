import json

with open('youtube_example.json', 'r') as json_file:
    i = json.load(json_file)

print(i);