# Get the actual CKL template checklist file text and save to a file
# API call from Developer's Guide: /api/external/template/{internalStringId}/?applicationKey={applicationKey}
# ex: python3 downloadChecklistTemplateCKLFile.py http://192.168.13.111:8080 627d44fbff17ea6dfdf0d702 openrmfprosvc hvs.xxxxxxxxxxx > ../download/mytemplatechecklist.ckl

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/template/" + sys.argv[2] + "/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/xml;charset=utf-8"
headers["Authorization"] = "Bearer " + sys.argv[4]
resp = requests.get(url, headers=headers)

print(resp.text)