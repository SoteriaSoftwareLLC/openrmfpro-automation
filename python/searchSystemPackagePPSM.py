# list the ports, protocols, and services in a system package
# ex: python3 searchSystemPackagePPSM.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import json
from prettytable import PrettyTable 
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/ppsm/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
portTable = PrettyTable(["Hostname"])

for element in json_object:
    port = int(element['lowPortNumber'])
    hostname = element['hostname']

    if int(sys.argv[5]) == port:
        portTable.add_row([hostname])

print(portTable)