import requests

#print("Hi this is a python request")

url = 'https://talkpython.fmx'

resp = requests.get(url)

print(resp)
