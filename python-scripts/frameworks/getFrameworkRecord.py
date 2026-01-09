# get the framework record
# API call from Developer's Guide: /api/external/controls/framework/{frameworkId}/?applicationKey={applicationKey}
# ex: python3 getFrameworkRecord.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx 68bb00b05c51ab74f106611b

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 4:
    print("Usage: python3 getFrameworkRecord.py <URL> <applicationKey> <token> <frameworkId>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
framework_id = sys.argv[4]

endpoint = "/api/external/controls/framework/{frameworkId}/"
url = f"{base_url}{endpoint.replace('{frameworkId}', framework_id)}"

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
        print("Error retrieving Framework Record:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")