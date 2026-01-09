# get the locked vulnerabilities
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/lockedvulnerabilities/?applicationKey={applicationKey}
# ex: python3 getLockedVulns.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 4:
    print("Usage: python3 getLockedVulns.py <URL> <applicationKey> <token> <systemKey>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]

endpoint = "/api/external/systempackage/{systemKey}/lockedvulnerabilities/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key)}"

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
        print("Error retrieving locked vulnerabilities:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")