import json

text_json = '''{
   "demo": "Processing JSON in Python",
"instructor": "Michael",
   "duration": 5.0
}'''

print('---------------- RAW JSON -----------')
print(type(text_json),text_json)
print('-------------------------------------')

data = json.loads(text_json)

print(type(data),data)
