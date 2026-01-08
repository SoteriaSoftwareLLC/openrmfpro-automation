# list checklist templates by DISA, CIS, Custom or Organizational
# API call from Developer's Guide: /api/external/templates/{templateType}?applicationKey={applicationKey}
# API call from Developer's Guide: /api/external/templates/disa/?applicationKey={applicationKey}&searchString=xxxxxxxxxxxxxxx
# ex: python3 listTemplateChecklist.py http://192.168.13.111:8080 disa openrmfprosvc  hvs.xxxxxxxxxxxxxxxx Cisco

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/templates/" + sys.argv[2]+ "/?applicationKey=" + sys.argv[3] + "&searchString=" + sys.argv[5]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))