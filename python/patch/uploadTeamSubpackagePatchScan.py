# Upload Nessus patch scan results *.nessus file
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/teamsubpackage/{teamKey}/patchscan/?applicationKey={applicationKey}
# ex: python3 uploadTeamSubpackagePatchScan.py http://192.168.13.111:8080 companyinfra network team openrmfprosvc hvs.xxxxxxxxxxxxxxxx ../../data/patch-vulnerability-scans/  DEGTHAT-2023-May.nessus

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/teamsubpackage/" + sys.argv[3] + "/patchscan/?applicationKey=" + sys.argv[4]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[5]

# file name of file to be uploaded hosted locally in the same directory as the python code
with open(sys.argv[6] + sys.argv[7], "rb") as a_file:
    patchscanFile = {sys.argv[7] : a_file}
    resp = requests.post(url, headers=headers, files=patchscanFile)

print(resp.status_code)
print(resp.text)