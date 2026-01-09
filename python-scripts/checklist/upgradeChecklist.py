# upgrade a checklist
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/upgradechecklist/{checklistId}/?applicationKey={applicationKey}
# ex: python3 upgradeChecklist.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork 613607883e0fd5dc610cd067

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 5:
    print("Usage: python3 upgradeChecklist.py <URL> <applicationKey> <token> <systemKey> <checklistId>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
checklist_id = sys.argv[5]

endpoint = "/api/external/systempackage/{systemKey}/upgradechecklist/{checklistId}/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key).replace('{checklistId}', checklist_id)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.put(url, headers=headers)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print("Checklist upgrade initiated successfully (Status 200 OK).")
    else:
        print("Error initiating checklist upgrade:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")