# Upload a DISA .xml to create a DISA based checklist
# API call from Developer's Guide: /api/external/template/disa/?applicationKey={applicationKey}
# ex: python3 uploadDISAAudit.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxxxx ./filename.xml

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/template/disa/?applicationKey=" + sys.argv[2]

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer " + sys.argv[3]

resp = requests.post(url, headers=headers, files={'checklistFile': open(sys.argv[4], 'rb')})

print(resp.status_code)
print(resp.text)