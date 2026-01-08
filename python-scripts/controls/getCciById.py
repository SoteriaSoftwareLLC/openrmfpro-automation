# Get CCI By ID
# API call from Developer's Guide: GET /api/external/controls/cci/{cciId}/?applicationKey={applicationKey}
# ex: python3 getCciById.py http://192.168.13.111:8080 svcapi hvs.xxxxxxxxxxxxxx CCI-000001

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 5:
    print("Usage: python3 getCciById.py <URL> <applicationKey> <token> <cciId>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
cci_id = sys.argv[4]

endpoint = f"/api/external/controls/cci/{cci_id}/"
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
        print(f"Error retrieving CCI {cci_id}:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")
