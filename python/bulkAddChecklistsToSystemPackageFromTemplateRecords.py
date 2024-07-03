# To bulk add checklists from template records you can call the below API
# The Template IDs you can view by listing all templates or searching templates
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/bulkadd/?applicationKey={applicationKey}
# ex: python3 bulkAddChecklistsToSystemPackageFromTemplateRecords.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxx "61b9e3df407f722ecf0ca361,61b9e3d4407f722ecf0ca2b6,61b9e3dd407f722ecf0ca345" # "FILESVR1"

import sys
import requests
from requests.structures import CaseInsensitiveDict

# Assign the API variables that are needed within the request's URL
TemplateIds=sys.argv[5]
checklistHostname=sys.argv[6]

# Build the API URL in order to make the request
url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/bulkadd/?applicationKey=" + sys.argv[3]

# Assign the request headers for this particular API
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Authorization"] = "Bearer " + sys.argv[4]

data = "templateIds="+TemplateIds+"&checklistHostname="+checklistHostname

# Make the API request
resp = requests.post(url, headers=headers, data=data)

# print to the screen the status code (i.e. 200, 400, 404, etc)
print(resp.status_code)

#print(resp.json)
print(resp.text)