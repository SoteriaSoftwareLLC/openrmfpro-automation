# check for a checklist upgrade
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/checkforupgrade/?applicationKey={applicationKey}
# ex: python3 checkChecklistUpgrade.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork "MSIE 11 STIG" "R4 dated 27 Apr 2023" 2

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 7:
    print("Usage: python3 checkChecklistUpgrade.py <URL> <applicationKey> <token> <systemKey> <stigType> <stigRelease> <stigVersion>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
stig_type = sys.argv[5]
stig_release = sys.argv[6]
stig_version = sys.argv[7]

endpoint = "/api/external/systempackage/{systemKey}/checkforupgrade/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key)}"

params = {
    "applicationKey": app_key,
    "stigType": stig_type,
    "stigRelease": stig_release,
    "stigVersion": stig_version
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
        print("Error checking for upgrade:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")