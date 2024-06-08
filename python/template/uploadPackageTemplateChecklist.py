# Upload checklist for System Package Template
# ex: python3 uploadPackageTemplateChecklist.py http://192.168.13.111:8080 package-key openrmfprosvc hvs.xxxxxxxxxxxxxxxx "My title" "My description" ../../data/ checklist.ckl

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/template/systempackage/" + sys.argv[2] + "/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer " + sys.argv[4]
headers["Accept"] = "application/json"

# file name of file to be uploaded hosted locally in the same directory as the python code
multipart_form_data = {
    'checklistFile': (sys.argv[8], open(sys.argv[7] + sys.argv[8], 'rb')),
    'title': (None, sys.argv[5]),
    'description': (None, sys.argv[6]),
}

resp = requests.post(url, headers=headers, files=multipart_form_data)

print(resp.status_code)
print(resp.text)