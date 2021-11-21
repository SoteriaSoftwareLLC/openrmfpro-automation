import requests
from requests.structures import CaseInsensitiveDict

url = "http://192.168.13.114:8080/api/external/systempackage/degthatnetwork/checklists/?applicationKey=degthatuploader"

headers = CaseInsensitiveDict()

headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer s.Fl0KfrDNJwa2OHlt3RoFbF84"
resp = requests.get(url, headers=headers)

# print(resp.status_code)
print(resp.text)