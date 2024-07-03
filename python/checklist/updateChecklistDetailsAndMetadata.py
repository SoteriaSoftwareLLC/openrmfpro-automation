# Update the hostname, MAC, IP, role, Asset Type, and other data within the specified checklist
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/checklist/{checklistId}/details/?applicationKey={applicationKey}
# ex: python3 updateChecklistDetailsAndMetadata.py http://192.168.13.111:8080 companyinfra 627d44fbff17ea6dfdf0d702 "desktop" true openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import requests
from requests.structures import CaseInsensitiveDict
from html import escape

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/checklist/" + sys.argv[3] + "/details/?applicationKey=" + sys.argv[6]

data = "tagList=" + escape(sys.argv[4]) + "&locked=" + escape(sys.argv[5])

# Assign the request headers for this particular API
headers = CaseInsensitiveDict() # Does not change
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[7]
headers["Content-Type"] = "application/x-www-form-urlencoded"

# Make the API request
resp = requests.put(url, headers=headers, data=data)

# print to the screen the status code (i.e. 200, 400, 404, etc)
print(resp.status_code)
print(resp.text)