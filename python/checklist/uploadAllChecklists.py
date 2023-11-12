# Upload a folder of SCAP XCCDF XML data, CKL data, or Audit Compliance .nessus data
# ex: python3 uploadAllChecklists.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxxxxx ../data/checklists/ 

import sys
import requests
import os
import glob
from requests.structures import CaseInsensitiveDict


url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/scapchecklist/?applicationKey=" + sys.argv[3]
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

# file name of checklist file to be uploaded hosted locally, passing in the directory name and filename
for file in glob.glob(sys.argv[5] + '*.*', recursive=False):
    with open(file, "rb") as a_file:
        checklistFile = {file : a_file}
        resp = requests.post(url, headers=headers, files=checklistFile)
        print(str(resp.status_code) + " Checklist " + os.path.basename(file) + " uploaded")