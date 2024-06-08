# Upload a Mitigation Statement List file
# ex: python3 uploadSystemPackageMitigationStatementList.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxxxx  ../../data/Mitigations/  degthatnetwork-mitigationlist.xlsx

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/mitigationstatements/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

# file name of file to be uploaded hosted locally
with open(sys.argv[5] + sys.argv[6], "rb") as a_file:
    mitigationFile = {sys.argv[6] : a_file}
    resp = requests.post(url, headers=headers, files=mitigationFile)

print(resp.status_code)
print(resp.text)