# Retrieve the list of team subpackage checklist and device/hardware items for a given system package
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/teamsubpackage/items/?applicationKey={applicationKey}applicationKey}&page=1&teamKey={teamKey}&itemType={itemTypeId}
# ex: python3 getListOfTeamSubPackageItems.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxx teamKey 10
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/teamsubpackage/items/?applicationKey=" + sys.argv[3] + "&page=1&teamKey=" + sys.argv[5] + "&itemType=" + sys.argv[6]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

# print(resp.status_code)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))