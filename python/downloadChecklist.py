import requests
from requests.structures import CaseInsensitiveDict

CheckListID = "61756e6a7008d30206c497bc"

url = "http://192.168.13.114:8080/api/external/systempackage/degthatnetwork/checklist/"+ CheckListID + "/?applicationKey=degthatuploader"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/xml;charset=utf-8"
headers["Authorization"] = "Bearer s.xxxxxxxxxxxxxxxxxxxxxxx"
resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.json)
print(resp.text)