# list all the notifications this user can view
# API call from Developer's Guide: /api/external/notifications/?applicationKey={applicationKey}
# API call from Developer's Guide: /api/external/notifications/?applicationKey={applicationKey}&bShowAll=true&systemKey=degthatnetwork&notificationType=poam
# API call from Developer's Guide: /api/external/notifications/?applicationKey={applicationKey}&bShowAll=true&notificationType=poam
# ex: python3 listNotifications.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/notifications/?applicationKey=" + sys.argv[2]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[3]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))