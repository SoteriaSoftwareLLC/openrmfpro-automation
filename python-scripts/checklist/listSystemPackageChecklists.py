# list all the checklists in a system package
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/checklists/?applicationKey={applicationKey}&page=1&limit=50&searchString=zzzzzzzzzzzzzzzz
# ex: python3 listSystemPackageChecklists.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxx 1 50
# current page of the results starts with page 1

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/checklists/?applicationKey=" + sys.argv[3] + "&page=" + sys.argv[5] + "&limit=" + sys.argv[6]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

# print(resp.status_code)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))