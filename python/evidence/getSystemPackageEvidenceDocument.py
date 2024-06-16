# get a single the system package Evidence record
# get the Internal Id String from the "List" evidence
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/evidence/{evidenceId}/?applicationKey={applicationKey}
# ex: python3 getSystemPackageEvidenceDocument.py http://192.168.13.111:8080 companyinfra 64a41c62a61876599144ca17 openrmfprosvc hvs.xxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/evidence/" + sys.argv[3] + "?applicationKey=" + sys.argv[4]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[5]

resp = requests.get(url, headers=headers)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))