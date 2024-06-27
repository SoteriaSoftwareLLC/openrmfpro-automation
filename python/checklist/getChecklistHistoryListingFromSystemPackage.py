# list the checklist history from the checklist history listing
# get the Internal Id String from the "List" checklists
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/checklistrecord/{internalIdString}/history/?applicationKey={applicationKey}
# ex: python3 getChecklistHistoryListingFromSystemPackage.py http://192.168.13.111:8080 companyinfra 627d44fbff17ea6dfdf0d702 openrmfprosvc hvs.xxxxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/checklistrecord/" + sys.argv[3]+ "/history/?applicationKey=" + sys.argv[4]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[5]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))