# get the severity override vulnerabilities
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/checklistvulnoverride/?applicationKey={applicationKey}
# ex: python3 getSeverityOverrideVulns.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork true true true true true true 1 50 

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 14:
    print(
        "Usage: python3 getSeverityOverrideVulns.py "
        "<URL> <applicationKey> <token> <systemKey> "
        "<notafinding> <open> <notapplicable> <notreviewed> "
        "<category1> <category2> <category3> <page> <limit> <searchString>"
    )
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
not_a_finding = sys.argv[5]
open_status = sys.argv[6]
not_applicable = sys.argv[7]
not_reviewed = sys.argv[8]
category1 = sys.argv[9]
category2 = sys.argv[10]
category3 = sys.argv[11]
page = sys.argv[12]
limit = sys.argv[13]
search_string = sys.argv[14]

endpoint = "/api/external/systempackage/{systemKey}/checklistvulnoverride/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key)}"

params = {
    "applicationKey": app_key,
    "notafinding": not_a_finding,
    "open": open_status,
    "notapplicable": not_applicable,
    "notreviewed": not_reviewed,
    "category1": category1,
    "category2": category2,
    "category3": category3,
    "page": page,
    "limit": limit,
    "searchString": search_string
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
        print("Error retrieving severity override vulnerabilities:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")