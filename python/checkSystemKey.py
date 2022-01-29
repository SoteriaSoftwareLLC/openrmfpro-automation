import requests
from requests.structures import CaseInsensitiveDict

SystemKey = "degthatnetwork"

url = "http://192.168.13.114:8080/api/external/systempackage/keycheck/"+SystemKey+"/?applicationKey=degthatuploader"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer s.xxxxxxxxxxxxxxxxxxxxxxx"

resp = requests.get(url, headers=headers)

print(resp.status_code)
#print(resp.json)
print(resp.text)
