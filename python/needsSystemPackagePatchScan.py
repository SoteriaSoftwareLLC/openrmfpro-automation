# list the hardware devices in a system package
# ex: python3 needsSystemPackagePatchScan.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxx

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
    patchscan = element['patchscan'] 
    hostname = element['hostname'] 

    if not(bool(patchscan)): #check if it does not have a patch scan
        hardwareTable.add_row([hostname])

print(hardwareTable)