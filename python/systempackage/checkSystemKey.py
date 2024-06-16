# Check if a system package key is available for adding a new system package
# Make sure you have SystemPackageAdministrator Role
# API call from Developer's Guide: /api/external/systempackage/keycheck/{systemKey}/?applicationKey={applicationKey}
# ex: python3 checkSystemKey.py http://192.168.13.111:8080 machinabio openrmfprosvc hvs.xxxxxxx

import sys
import requests
from requests.structures import CaseInsensitiveDict

SystemKey = "degthatnetwork"

url = sys.argv[1] + "/api/external/systempackage/keycheck/" + sys.argv[2] + "/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

print(resp.status_code)
print(resp.text)