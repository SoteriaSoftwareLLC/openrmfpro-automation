# list the system package POAM records
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/poam/?applicationKey={applicationKey}&days=nn&devicename-xxxxxxxxxxxxxx
# ex: python3 listSystemPackagePOAM.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxx 180

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/poam/?applicationKey=" + sys.argv[3] + "&days=" + sys.argv[5]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))