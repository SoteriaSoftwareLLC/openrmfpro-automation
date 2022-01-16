import requests
from requests.structures import CaseInsensitiveDict

url = "http://192.168.13.114:8080/api/external/systempackage/degthatnetwork/teamsubpackage/networkteam/patchscan/?applicationKey=degthatuploader"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer s.xxxxxxxxxxxxxxxxxxxxxxx"

# file name of checklist file to be uploaded hosted locally in the same directory as the python code
with open("../data/nessus-scans/MachinaBio_System_Scan_Post-Patch-Oct_2021.nessus", "rb") as a_file:
    patchscanFile = {"MachinaBio_System_Scan_Post-Patch-Oct_2021.nessus" : a_file}
    resp = requests.post(url, headers=headers, files=patchscanFile)

print(resp.status_code)
print(resp.text)