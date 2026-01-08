# list the control family sections
# API call from Developer's Guide: /api/external/controls/family/{familyId}/?applicationKey={applicationKey}
# ex: python3 listControlFamilySections.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx 68cdb5fc040f5d693f2ea161

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 4:
    print("Usage: python3 listControlFamilySections.py <URL> <applicationKey> <token> <familyId>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
family_id = sys.argv[4]

endpoint = "/api/external/controls/family/{familyId}/"
url = f"{base_url}{endpoint.replace('{familyId}', family_id)}"

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
        print("Error retrieving Control Family Sections:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")