# create an approved PPS record
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/pps/?applicationKey={applicationKey}
# ex: python3 createApprovedPPSRecord.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork "My Approved PPS Record" UDP 80 80 "My Service Name"

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 8:
    print("Usage: python3 createApprovedPPSRecord.py <URL> <applicationKey> <token> <systemKey> <title> <protocol> <lowPort> <highPort> <serviceName>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]

data = {
    "title": sys.argv[5],
    "protocol": sys.argv[6],
    "lowPort": sys.argv[7],
    "highPort": sys.argv[8],
    "serviceName": sys.argv[9]
}

endpoint = "/api/external/systempackage/{systemKey}/pps/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.post(url, headers=headers, data=data)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print("Approved PPS record created successfully.")
    else:
        print("Error creating Approved PPS record:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")