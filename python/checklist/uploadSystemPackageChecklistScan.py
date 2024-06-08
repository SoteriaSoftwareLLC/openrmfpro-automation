# Upload SCAP XCCDF XML data, CKL data, or Audit Compliance .nessus data
# ex: python3 uploadSystemPackageChecklistScan.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxxxxx ../../data/checklists/ MachinaBio_System_Scan_Post-Patch-Dec_2020.nessus

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/scapchecklist/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

# file name of checklist file to be uploaded hosted locally, passing in the directory name and filename
with open(sys.argv[5] + sys.argv[6], "rb") as a_file:
    checklistFile = {sys.argv[6] : a_file}
    resp = requests.post(url, headers=headers, files=checklistFile)

print(resp.status_code)
print(resp.text)