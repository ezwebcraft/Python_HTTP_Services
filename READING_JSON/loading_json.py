import json
import datetime


text_json = """{
    "demo": "Processing JSON in Python",
    "instructor": "Michael",
    "duration": 5.0
    }
"""

print(type(text_json), text_json)

print()

data = json.loads(text_json)

print(type(data), data)

print()

instructor = data.get("instructor", "Nothing Found")

print()

print("instructor is: {}".format(instructor))

print(data["demo"])

print()
data["time"] = str(datetime.datetime.now())

print(data)
