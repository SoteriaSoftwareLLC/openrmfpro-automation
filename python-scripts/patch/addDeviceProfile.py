# add a device profile
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/deviceprofile/?applicationKey={applicationKey}
# ex: python3 addDeviceProfile.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork 

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 6:
    print("Usage: python3 addDeviceProfile.py <URL> <applicationKey> <token> <systemKey>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]

# JSON Payload for the request body
payload = {
    "title": "My New Device Profile",
    "description": "Device Profile Description for New Servers",
    "allowedPPS": [
        {
            "lowport": "443",
            "highPort": "8443",
            "protocol": "udp",
            "serviceName": "My Service Name"
        },
        {
            "lowport": "80",
            "highPort": "88",
            "protocol": "tcp",
            "serviceName": "Second Service Name"
        }
    ]
}

endpoint = "/api/external/systempackage/{systemKey}/deviceprofile/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {token}"
headers["Content-Type"] = "application/json"

try:
    resp = requests.post(url, headers=headers, json=payload)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print("Device Profile added successfully.")
    else:
        print("Error adding Device Profile:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")