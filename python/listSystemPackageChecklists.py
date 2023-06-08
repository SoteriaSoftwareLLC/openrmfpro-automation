# list all the checklists in a system package
# ex: python3 listSystemPackageChecklists.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxx 0 50

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