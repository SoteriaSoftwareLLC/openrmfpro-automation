# update a hardware record
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/hardwareasset/{assetId}/?applicationKey={applicationKey}
# ex: python3 updateHardwareRecord.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork 6671c5b3b4268ee3a8c11d57 APPWKS_UPDATED Linux 22.04 LTS true Web Server 192.168.1.100,10.0.0.5 00:00:00:00:00:00 "" Lenovo WKS22234 2342343-PV1 "This is the main IIS web server for application hosting internally." tag1,tag2

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 17:
    print("Usage: python3 updateHardwareRecord.py <URL> <applicationKey> <token> <systemKey> <assetId> <newAssetName> <operatingSystem> <virtualServer> <purpose> <ipAddresses> <macAddresses> <firmware> <manufacturer> <modelNumber> <serialNumber> <description> <tags>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
asset_id = sys.argv[5]
new_asset_name = sys.argv[6]
operating_system = sys.argv[7]
virtual_server = sys.argv[8]
purpose = sys.argv[9]
ip_addresses = sys.argv[10]
mac_addresses = sys.argv[11]
firmware = sys.argv[12]
manufacturer = sys.argv[13]
model_number = sys.argv[14]
serial_number = sys.argv[15]
description = sys.argv[16]
tags = sys.argv[17]

data = {
    "assetName": new_asset_name,
    "operatingSystem": operating_system,
    "virtualServer": virtual_server,
    "purpose": purpose,
    "ipAddresses": ip_addresses,
    "macAddresses": mac_addresses,
    "firmware": firmware,
    "manufacturer": manufacturer,
    "modelNumber": model_number,
    "serialNumber": serial_number,
    "description": description,
    "tagList": tags
}

endpoint = "/api/external/systempackage/{systemKey}/hardwareasset/{assetId}/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key).replace('{assetId}', asset_id)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.put(url, headers=headers, data=data)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print(f"Hardware record for ID {asset_id} updated successfully.")
    else:
        print("Error updating hardware record:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")