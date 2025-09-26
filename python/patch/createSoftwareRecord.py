# create a software record
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/softwareasset/?applicationKey={applicationKey}
# ex: python3 createSoftwareRecord.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork APPWKS Firefox 119.0.0 30 10/01/2023 #ABC-123

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 8:
    print("Usage: python3 createSoftwareRecord.py <URL> <applicationKey> <token> <systemKey> <deviceName> <softwareName> <softwareVersion> <assetType> <installedOn> <approvalReference>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
device_name = sys.argv[5]
software_name = sys.argv[6]
software_version = sys.argv[7]
asset_type = sys.argv[8]
installed_on = sys.argv[9]
approval_reference = sys.argv[10]

data = {
    "deviceName": device_name,
    "softwareName": software_name,
    "softwareVersion": software_version,
    "assetType": asset_type,
    "installedOn": installed_on,
    "approvalReference": approval_reference
}

endpoint = "/api/external/systempackage/{systemKey}/softwareasset/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.post(url, headers=headers, data=data)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print(f"Software record for {software_name} on {device_name} created successfully.")
    else:
        print("Error creating software record:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")