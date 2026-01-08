# To delete the cyber readiness settings and weights specified for this system package and use the site-wide default settings for the cyber readiness score calculation
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/readinesssettings/?applicationKey={applicationKey}
# ex: python3 deleteCyberReadinessSettings.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/readinesssettings/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.delete(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))