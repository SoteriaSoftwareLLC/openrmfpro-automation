# score history of a particular source project for the other technology vulnerabilities
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/techvulnerabilityscorehistory/{categoryType}/sourceproject/?source={sourcename}&project={projectname}&applicationKey={applicationKey}
# for the source and project, you may need to put double quotes "" around the data if containing spaces or special characters
# ex: python3 listSystemPackageTechVulnerabilitiesScoreHistoryBySourceAndProject.py http://192.168.13.111:8080 companyinfra 10 "sourcename" "projectname" openrmfprosvc hvs.xxxxxxxxxxxxxx

## v2.10.02 change for a bug on passing parameters via URL

import sys
import json
import urllib.parse
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/techvulnerabilityscorehistory/" + sys.argv[3] + "/sourceproject/?source=" + urllib.parse.quote_plus(sys.argv[4]) + "&project=" + urllib.parse.quote_plus(sys.argv[5]) + "&applicationKey=" + sys.argv[6]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[7]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))