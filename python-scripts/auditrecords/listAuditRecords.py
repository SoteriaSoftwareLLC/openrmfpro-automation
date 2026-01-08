# list audit records in JSON format
# API call from Developer's Guide: /api/external/audit/?applicationKey={applicationKey}
# ex: python3 listAuditRecords.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/audit/?applicationKey=" + sys.argv[2]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[3]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))