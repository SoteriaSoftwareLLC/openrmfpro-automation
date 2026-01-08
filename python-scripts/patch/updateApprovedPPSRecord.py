# update an approved PPS record
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/pps/{ppsId}/?applicationKey={applicationKey}
# ex: python3 updateApprovedPPSRecord.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork 6671c5b3b4268ee3a8c11d57 "My Updated PPS Record" UDP 80 80 "My Service Name"

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 10:
    print("Usage: python3 updateApprovedPPSRecord.py <URL> <applicationKey> <token> <systemKey> <ppsId> <title> <protocol> <lowPort> <highPort> <serviceName>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
pps_id = sys.argv[5]

data = {
    "title": sys.argv[6],
    "protocol": sys.argv[7],
    "lowPort": sys.argv[8],
    "highPort": sys.argv[9],
    "serviceName": sys.argv[10]
}

endpoint = "/api/external/systempackage/{systemKey}/pps/{ppsId}/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key).replace('{ppsId}', pps_id)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.put(url, headers=headers, data=data)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print(f"Approved PPS record for ID {pps_id} updated successfully.")
    else:
        print("Error updating Approved PPS record:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")