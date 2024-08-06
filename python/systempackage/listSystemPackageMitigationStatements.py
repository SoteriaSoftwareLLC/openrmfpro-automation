# Get the mitigation statements listing of a system package for display or reporting
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/mitigation/?applicationKey={applicationKey}
# ex: python3 listSystemPackageMitigationStatements.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
 
url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/mitigation/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))