# list the system package Evidence records total file count and total file size
# ex: python3 getSystemPackageEvidenceTotalSize.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/evidence/?general=true&checklist=true&statement=true&poam=true&applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

# store the total size and add it up
totalSize = 0
totalFiles = 0

json_object = json.loads(resp.text)
for element in json_object:  # iterate on each element of the list
    totalSize = totalSize + element['fileSize'] # add to the going total
    totalFiles = totalFiles + 1

print("Total Files: " + str(totalFiles))  # print it
print("Total Size:  " + str(totalSize) + " KB")  # print it