# Upload a piece of Evidence to the POAM category of evidence documents, passing in the # POAM Item Id generated in the listing
# ex: python3 uploadSystemPackagePOAMEvidence.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxxxx 125 "my-title" "my-description-text" ../../data/evidence/ Disaster-Recovery-Plan.pdf

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/evidence/poam/" + sys.argv[5] + "/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

# file name of file to be uploaded hosted locally in the same directory as the python code
multipart_form_data = {
    'evidenceFile': (sys.argv[9], open(sys.argv[8] + sys.argv[9], 'rb')),
    'allowOverwrite': (None, 'false'),
    'title': (None, sys.argv[6]),
    'description': (None, sys.argv[7]),
}

resp = requests.post(url, headers=headers, files=multipart_form_data)

print(resp.status_code)
print(resp.text)