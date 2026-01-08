# list the system package Evidence types of files
# ex: python3 getSystemPackageEvidenceFileTypes.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/evidence/?general=true&checklist=true&statement=true&poam=true&applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

# store the total sizes and add it up
fileTypeList = []

json_object = json.loads(resp.text)
for element in json_object:  # iterate on each element of the list
   if element['fileTypeString'] not in fileTypeList:
    fileTypeList.append(element['fileTypeString'])

print("------------------------------------")
print(f"Types of Evidence Files: {fileTypeList}")
print("------------------------------------")