import requests
from requests.structures import CaseInsensitiveDict

CheckListRecord = "61ae0f58870794d9304bb15a"

url = "http://192.168.13.114:8080/api/external/systempackage/aspireninetest/"+ CheckListRecord + "/?applicationKey=aspirenineuploader"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer s.eSAczEu8a5vAOHfLRz09GVPj"

resp = requests.get(url, headers=headers)

print(resp.status_code)
#print(resp.json)
print(resp.text)