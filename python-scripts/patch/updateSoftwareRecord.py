# update a software record
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/softwareasset/{assetId}/?applicationKey={applicationKey}
# ex: python3 updateSoftwareRecord.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork 6671c5b3b4268ee3a8c11d57 APPWKS Firefox 120.0.0 30 #ABC-123

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 9:
    print("Usage: python3 updateSoftwareRecord.py <URL> <applicationKey> <token> <systemKey> <assetId> <deviceName> <softwareName> <softwareVersion> <assetType> <approvalReference>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
asset_id = sys.argv[5]
device_name = sys.argv[6]
software_name = sys.argv[7]
software_version = sys.argv[8]
asset_type = sys.argv[9]
approval_reference = sys.argv[10]

data = {
    "deviceName": device_name,
    "softwareName": software_name,
    "softwareVersion": software_version,
    "assetType": asset_type,
    "approvalReference": approval_reference
}

endpoint = "/api/external/systempackage/{systemKey}/softwareasset/{assetId}/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key).replace('{assetId}', asset_id)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.put(url, headers=headers, data=data)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print(f"Software record for ID {asset_id} updated successfully.")
    else:
        print("Error updating software record:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")