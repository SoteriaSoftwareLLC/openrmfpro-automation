# list all the other tech vulnerabilities in a system package
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/techvulnerabilitydata/?applicationKey={applicationKey}&categoryType={categoryType}
# ex: python3 listSystemPackageTechVulnerabilities.py http://192.168.13.111:8080 companyinfra 10 openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/techvulnerabilitydata/?categoryType=" + sys.argv[3] + "&applicationKey=" + sys.argv[4]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[5]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))