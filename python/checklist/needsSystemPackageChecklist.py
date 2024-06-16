# list the hardware devices in a system package needing a checklist or compliance scan
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/hardware/?applicationKey={applicationKey}&devicename={hostname}
# ex: python3 needsSystemPackageChecklist.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import json
from prettytable import PrettyTable 
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
# print(json.dumps(json_object, indent=1))

hardwareTable = PrettyTable(["Hostname"])

for element in json_object:  # iterate on each element of the list
    checklist = element['checklist'] 
    hostname = element['hostname'] 

    if not(bool(checklist)): #check if it does not have a patch scan
        hardwareTable.add_row([hostname])

print(hardwareTable)