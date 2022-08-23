import requests

url= "https://generator.swagger.io/api/swagger.json"
response=requests.get(url)
print(response)
print(response.content)
print(response.headers)
print(response.status_code)
assert response.status_code == 200