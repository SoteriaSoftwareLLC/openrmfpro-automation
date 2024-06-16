# Upload a Compliance Statement List file
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/compliancestatements/?applicationKey={applicationKey}
# ex: python3 uploadSystemPackageComplianceStatementList.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxxxx  ../../data/ComplianceData/ compliancetest-ComplianceStatements.xlsx

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/compliancestatements/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

# file name of file to be uploaded hosted locally in the same directory as the python code
with open(sys.argv[5] + sys.argv[6], "rb") as a_file:
    complianceFile = {sys.argv[6] : a_file}
    resp = requests.post(url, headers=headers, files=complianceFile)

print(resp.status_code)
print(resp.text)