# create a hardware record
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/hardwareasset/?applicationKey={applicationKey}
# ex: python3 createHardwareRecord.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork NEWSERVER01 Linux 22.04 LTS true Web Server 192.168.1.100,10.0.0.5 00:00:00:00:00:00 "" Lenovo WKS22234 2342343-PV1 "This is the main IIS web server for application hosting internally." tag1,tag2

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 16:
    print("Usage: python3 createHardwareRecord.py <URL> <applicationKey> <token> <systemKey> <assetName> <operatingSystem> <virtualServer> <purpose> <ipAddresses> <macAddresses> <firmware> <manufacturer> <modelNumber> <serialNumber> <description> <tags>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
asset_name = sys.argv[5]
operating_system = sys.argv[6]
virtual_server = sys.argv[7]
purpose = sys.argv[8]
ip_addresses = sys.argv[9]
mac_addresses = sys.argv[10]
firmware = sys.argv[11]
manufacturer = sys.argv[12]
model_number = sys.argv[13]
serial_number = sys.argv[14]
description = sys.argv[15]
tags = sys.argv[16]

data = {
    "assetName": asset_name,
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

endpoint = "/api/external/systempackage/{systemKey}/hardwareasset/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.post(url, headers=headers, data=data)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print(f"Hardware record for {asset_name} created successfully.")
    else:
        print("Error creating hardware record:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")