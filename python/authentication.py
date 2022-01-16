import requests
from requests.structures import CaseInsensitiveDict

url = "http://192.168.13.114:8080/api/external/testauthentication"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Authorization"] = "Bearer s.xxxxxxxxxxxxxxxxxxxxxxx"

data = "applicationKey=degthatuploader"

resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)