# create a mitigation statement
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/mitigationstatement/?applicationKey={applicationKey}
# ex: python3 createMitigationStatement.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork "Inherited from Platform" Infrastructure "This is inherited from the platform we are using."

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 7:
    print("Usage: python3 createMitigationStatement.py <URL> <applicationKey> <token> <systemKey> <mitigationTitle> <mitigationCategory> <mitigationStatement>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]

# Required data
data = {
    "mitigationTitle": sys.argv[5],
    "mitigationCategory": sys.argv[6],
    "mitigationStatement": sys.argv[7]
}

endpoint = "/api/external/systempackage/{systemKey}/mitigationstatement/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.post(url, headers=headers, data=data)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print("Mitigation Statement created successfully.")
    else:
        print("Error creating Mitigation Statement:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")