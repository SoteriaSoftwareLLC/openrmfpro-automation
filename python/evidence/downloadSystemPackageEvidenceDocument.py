# get a single the system package Evidence record and download that proper file with proper name and content type
# get the Internal Id String from the "List" evidence
# ex: python3 downloadSystemPackageEvidenceDocument.py http://192.168.13.111:8080 companyinfra 64a4131da61876599144c9fb openrmfprosvc hvs.xxxxxxxxx

import sys
import json
import urllib.request
import shutil
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/evidence/" + sys.argv[3] + "?applicationKey=" + sys.argv[4]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[5]

resp = requests.get(url, headers=headers)

json_object = json.loads(resp.text)
filename = json_object['filename']
contentType = json_object['contentType']

downloadUrl = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/evidence/" + sys.argv[3] + "/download/?applicationKey=" + sys.argv[4]

# now get the file with the valid content type
fileHeaders = CaseInsensitiveDict()
fileHeaders["Accept"] = contentType
fileHeaders["Authorization"] = "Bearer " + sys.argv[5]
# open in binary mode
with open("../download/" + filename, "wb") as file:
    # get request
    response = requests.get(downloadUrl, headers=fileHeaders)
    # write to file
    file.write(response.content)