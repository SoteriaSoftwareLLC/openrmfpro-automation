# Upload checklist for Organization Template
# ex: python3 uploadOrganizationTemplateChecklist.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxxxx "My title" "My description" ../../data/ checklist.ckl

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/template/organization/?applicationKey=" + sys.argv[2]

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer " + sys.argv[3]
headers["Accept"] = "application/json"

# file name of file to be uploaded hosted locally in the same directory as the python code
multipart_form_data = {
    'checklistFile': (sys.argv[7], open(sys.argv[6] + sys.argv[7], 'rb')),
    'title': (None, sys.argv[4]),
    'description': (None, sys.argv[5]),
}

resp = requests.post(url, headers=headers, files=multipart_form_data)

print(resp.status_code)
print(resp.text)