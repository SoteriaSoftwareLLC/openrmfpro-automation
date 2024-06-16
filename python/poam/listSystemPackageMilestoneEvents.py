# list the system package milestone records
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/milestoneevents/?applicationKey={applicationKey}&days=nn
# ex: python3 listSystemPackageMilestoneEvents.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/milestoneevents/?includePastEvents=false&applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))