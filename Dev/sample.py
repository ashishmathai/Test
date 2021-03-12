import requests

url = "https://www.google.com"
headers = {'User-Agent': 'Chrome-87'}

res = requests.get(url, headers=headers)

print (res.text)
