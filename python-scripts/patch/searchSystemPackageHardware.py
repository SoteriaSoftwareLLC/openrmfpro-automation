# list the hardware devices in a system package
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/hardware/?applicationKey={applicationKey}&devicename={hostname}
# ex: python3 searchSystemPackageHardware.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxx "red hat"

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

for element in json_object:
    hostname = element['hostname']
    operatingSystem = element['operatingSystem']

    if operatingSystem and sys.argv[5].lower() in operatingSystem.lower():
        hardwareTable.add_row([hostname])

print(hardwareTable)