# list the hardware devices in a system package
# ex: python3 listSystemPackageHardwareScan.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/hardware/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))

for element in json_object:  # iterate on each element of the list
    hostname = element['hostname'] # get hostname
    patchscan = element['patchscan'] # get patch scan
    checklist = element['checklist'] # get checklist
    print("Hostname: " + hostname) # print it out

    if (bool(patchscan)): #check if it has a patch scan
        print("Patch Scan?: Yes")
    else:
        print("Patch Scan?: No")

    if (bool(checklist)): #check if it has a checklist
        print("Checklist?: Yes")
    else:
        print("Checklist?: No")

    print("-------------------------")