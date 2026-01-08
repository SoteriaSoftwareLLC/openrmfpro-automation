# update a PPSM record
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/ppsm/{ppsmId}/?applicationKey={applicationKey}
# ex: python3 updatePPSMRecord.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork 6671c5b3b4268ee3a8c11d57 true true true true true true true true true true

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 21:
    print(
        "Usage: python3 updatePPSMRecord.py "
        "<URL> <applicationKey> <token> <systemKey> <ppsmId> "
        "<boundary1In> <boundary1Out> <boundary2In> <boundary2Out> "
        "<boundary3In> <boundary3Out> <boundary4In> <boundary4Out> "
        "<boundary5In> <boundary5Out> <boundary6In> <boundary6Out> "
        "<boundary7In> <boundary7Out> <boundary8In> <boundary8Out>"
    )
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
ppsm_id = sys.argv[5]
boundary1_in = sys.argv[6]
boundary1_out = sys.argv[7]
boundary2_in = sys.argv[8]
boundary2_out = sys.argv[9]
boundary3_in = sys.argv[10]
boundary3_out = sys.argv[11]
boundary4_in = sys.argv[12]
boundary4_out = sys.argv[13]
boundary5_in = sys.argv[14]
boundary5_out = sys.argv[15]
boundary6_in = sys.argv[16]
boundary6_out = sys.argv[17]
boundary7_in = sys.argv[18]
boundary7_out = sys.argv[19]
boundary8_in = sys.argv[20]
boundary8_out = sys.argv[21]

data = {
    "boundary1In": boundary1_in,
    "boundary1Out": boundary1_out,
    "boundary2In": boundary2_in,
    "boundary2Out": boundary2_out,
    "boundary3In": boundary3_in,
    "boundary3Out": boundary3_out,
    "boundary4In": boundary4_in,
    "boundary4Out": boundary4_out,
    "boundary5In": boundary5_in,
    "boundary5Out": boundary5_out,
    "boundary6In": boundary6_in,
    "boundary6Out": boundary6_out,
    "boundary7In": boundary7_in,
    "boundary7Out": boundary7_out,
    "boundary8In": boundary8_in,
    "boundary8Out": boundary8_out
}

endpoint = "/api/external/systempackage/{systemKey}/ppsm/{ppsmId}/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key).replace('{ppsmId}', ppsm_id)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.put(url, headers=headers, data=data)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print(f"PPSM record for ID {ppsm_id} updated successfully.")
    else:
        print("Error updating PPSM record:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")