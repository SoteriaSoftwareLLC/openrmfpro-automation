#Post a JSON record array payload to add / update ports, protocols, and services items in the host scan area for your system package
# API call from Developer's Guide:/api/external/systempackage/{systemKey}/ppsm/?applicationKey={applicationKey}
# ex: python3 uploadApprovedPortsAndProtocolsListFile.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/ppsm/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

# file name of PPSM file to be uploaded hosted locally, passing in the directory name and filename
with open(sys.argv[5] + sys.argv[6], "rb") as a_file:
    ppsFile = {sys.argv[6] : a_file}
    resp = requests.post(url, headers=headers, files=ppsFile)

print(resp.status_code)
print(resp.text)