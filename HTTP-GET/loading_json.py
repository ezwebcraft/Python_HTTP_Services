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

# Pull instructor data

instructor = data.get('instructor','SUBSTITUTE')

print("Your Instructor is {} ....".format(instructor))

# testing the json change data

data['instructor'] =  'Jeff'

new_json = json.dumps(data)

print(type(new_json),new_json)
