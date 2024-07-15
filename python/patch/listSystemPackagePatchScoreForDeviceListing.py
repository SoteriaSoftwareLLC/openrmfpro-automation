# Get the total patch vulnerability score broken out by devices for a system package
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/patchscore/devices/?applicationKey={applicationKey}&device={hostname}
# ex: python3 listSystemPackagePatchScoreForDeviceListing.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxx degthat

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/patchscore/devices/?applicationKey=" + sys.argv[3] + "&devices=" + sys.argv[5]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))