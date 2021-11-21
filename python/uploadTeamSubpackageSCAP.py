import requests
from requests.structures import CaseInsensitiveDict

url = "http://192.168.13.114:8080/api/external/systempackage/degthatnetwork/teamsubpackage/networkteam/scapchecklist/?applicationKey=degthatuploader"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer s.Fl0KfrDNJwa2OHlt3RoFbF84"

# file name of checklist file to be uploaded hosted locally in the same directory as the python code
with open("../data/scap-scans/DEGTHAT_SCC-5.0.1_2019-04-19_170849_XCCDF-Results_Windows_10_STIG-001.012.xml", "rb") as a_file:
    patchscanFile = {"DEGTHAT_SCC-5.0.1_2019-04-19_170849_XCCDF-Results_Windows_10_STIG-001.012.xml" : a_file}
    resp = requests.post(url, headers=headers, files=patchscanFile)

print(resp.status_code)
print(resp.text)