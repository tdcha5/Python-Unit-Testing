import requests

## base URL
url = "https://cat-fact.herokuapp.com" 

## send Get request
response = requests.get(url)
print(response)