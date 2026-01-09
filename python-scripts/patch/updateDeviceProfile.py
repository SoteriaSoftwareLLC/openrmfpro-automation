# update a device profile
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/deviceprofile/{profileId}/?applicationKey={applicationKey}
# ex: python3 updateDeviceProfile.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork 6671c5b3b4268ee3a8c11d57

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 6:
    print("Usage: python3 updateDeviceProfile.py <URL> <applicationKey> <token> <systemKey> <profileId>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
profile_id = sys.argv[5]

# JSON Payload for the request body
payload = {
    "title": "My Device Profile UPDATED",
    "description": "Device Profile Description UPDATED",
    "allowedPPS": [
        {
            "lowport": "443",
            "highPort": "8443",
            "protocol": "udp",
            "serviceName": "My Service Name"
        },
        {
            "lowport": "81",
            "highPort": "88",
            "protocol": "tcp",
            "serviceName": "Second Service Name"
        }
    ]
}

endpoint = "/api/external/systempackage/{systemKey}/deviceprofile/{profileId}/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key).replace('{profileId}', profile_id)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {token}"
headers["Content-Type"] = "application/json"

try:
    resp = requests.put(url, headers=headers, json=payload)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print(f"Device Profile for ID {profile_id} updated successfully.")
    else:
        print("Error updating Device Profile:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")