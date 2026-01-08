# delete a software record
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/softwareasset/{assetId}/?applicationKey={applicationKey}
# ex: python3 deleteSoftwareRecord.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork 6671c5b3b4268ee3a8c11d57

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 5:
    print("Usage: python3 deleteSoftwareRecord.py <URL> <applicationKey> <token> <systemKey> <assetId>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
asset_id = sys.argv[5]

endpoint = "/api/external/systempackage/{systemKey}/softwareasset/{assetId}/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key).replace('{assetId}', asset_id)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

try:
    # DELETE operation
    resp = requests.delete(url, headers=headers)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print(f"Software record for ID {asset_id} deleted successfully.")
    else:
        print("Error deleting software record:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")