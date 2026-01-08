# Get CCIs By Major Control
# API call from Developer's Guide: GET /api/external/controls/cciforcontrol/{control}/?applicationKey={applicationKey}
# ex: python3 getCcisByMajorControl.py http://192.168.13.111:8080 svcapi hvs.xxxxxxxxxxxxxx 68dee38349279abaa496b5e3 AC-1

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 5:
    print("Usage: python3 getCcisByMajorControl.py <URL> <applicationKey> <token> <frameworkId> <control>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
framework_id = sys.argv[4]
control = sys.argv[5]

endpoint = f"/api/external/controls/cciforcontrol/{framework_id}/control/{control}/"
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
        print(f"Error retrieving CCIs for control {control}:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")
