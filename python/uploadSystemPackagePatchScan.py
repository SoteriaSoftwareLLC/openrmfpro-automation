# Upload Nessus patch scan results *.nessus file, .xml Nexpose or .JSON universal patch format file
# ex: python3 uploadSystemPackageSCAP.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxxxx  ../data/scap-scans/  DEGTHAT_SCC-5.0.1_2019-04-19_170849_XCCDF-Results_Microsoft_Outlook_2016-001.003.xml

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/patchscan/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

# file name of file to be uploaded hosted locally in the same directory as the python code
with open(sys.argv[5] + sys.argv[6], "rb") as a_file:
    patchscanFile = {sys.argv[6] : a_file}
    resp = requests.post(url, headers=headers, files=patchscanFile)

print(resp.status_code)
json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))