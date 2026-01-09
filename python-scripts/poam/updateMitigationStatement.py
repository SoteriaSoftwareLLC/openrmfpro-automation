# update a mitigation statement
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/mitigationstatement/{statementId}/?applicationKey={applicationKey}
# ex: python3 updateMitigationStatement.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork 6671c5b3b4268ee3a8c11d57 "New Title" NewCategory "New updated statement"

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 8:
    print("Usage: python3 updateMitigationStatement.py <URL> <applicationKey> <token> <systemKey> <statementId> <mitigationTitle> <mitigationCategory> <mitigationStatement>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
statement_id = sys.argv[5]

data = {
    "mitigationTitle": sys.argv[6],
    "mitigationCategory": sys.argv[7],
    "mitigationStatement": sys.argv[8]
}

endpoint = "/api/external/systempackage/{systemKey}/mitigationstatement/{statementId}/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key).replace('{statementId}', statement_id)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.put(url, headers=headers, data=data)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print(f"Mitigation Statement for ID {statement_id} updated successfully.")
    else:
        print("Error updating Mitigation Statement:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")