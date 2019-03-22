import json

text_json = '''{
    "demo": "Processing JSON in Python",
    "instructor": "Michael",
    "duration": 5.0
    }
'''

print(type(text_json), text_json)

data = json.loads(text_json)

print(data)


print(data["demo"])
