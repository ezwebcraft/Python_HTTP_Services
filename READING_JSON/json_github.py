import requests

url = 'https://github.com/linuxbytes/Python_HTTP_Services'

response = requests.get(url)

print(response)