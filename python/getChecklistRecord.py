import requests
from requests.structures import CaseInsensitiveDict

CheckListRecord = "61ae0f58870794d9304bb15a"

url = "http://192.168.13.114:8080/api/external/systempackage/degthatnetwork/checklistrecord/"+ CheckListRecord + "/?applicationKey=degthatuploader"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer s.xxxxxxxxxxxxxxxxxxxxxxx"

resp = requests.get(url, headers=headers)

print(resp.status_code)
#print(resp.json)
print(resp.text)