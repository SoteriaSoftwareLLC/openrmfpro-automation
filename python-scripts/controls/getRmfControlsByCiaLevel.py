# Get a List of RMF Controls By CIA Level
# API call from Developer's Guide: GET /api/external/controls/rmf/confidentiality/{conLevel}/integrity/{intLevel}/availability/{availLevel}/?applicationKey={applicationKey}
# ex: python3 getRmfControlsByCiaLevel.py http://192.168.13.111:8080 svcapi hvs.xxxxxxxxxxxxxx low low low

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 7:
    print("Usage: python3 getRmfControlsByCiaLevel.py <URL> <applicationKey> <token> <conLevel> <intLevel> <availLevel>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
con_level = sys.argv[4]
int_level = sys.argv[5]
avail_level = sys.argv[6]

endpoint = f"/api/external/controls/rmf/confidentiality/{con_level}/integrity/{int_level}/availability/{avail_level}/"
url = f"{base_url}{endpoint}"

params = {
    "applicationKey": app_key
}

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.get(url, headers=headers, params=params)

    print(f"HTTP Status Code: {resp.status_code}")

    if resp.status_code == 200:
        json_object = resp.json()
        print(json.dumps(json_object, indent=1))
    else:
        print("Error retrieving RMF Controls by CIA Level:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")
