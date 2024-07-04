# Update the hostname, MAC, IP, role, Asset Type, and other data within the specified checklist
# Pass all the parameters or they will be put back to default
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/checklist/{checklistId}/details/?applicationKey={applicationKey}
# See the Developers Guide on allowed Technology Area, Asset Type, and Role

# ex: python3 updateChecklistDetailsAndMetadata.py http://192.168.13.111:8080 companyinfra 627d44fbff17ea6dfdf0d702 openrmfprosvc hvs.xxxxxxxxxxxxxx "MY-SERVER-NAME" "my-server-name.company.com" "Windows OS" "192.168.1.111" "" "false" "" "" "Computing" "Workstation" "desktop|windows"

import sys
import requests
import json
from requests.structures import CaseInsensitiveDict
from html import escape

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/checklist/" + sys.argv[3] + "/details/?applicationKey=" + sys.argv[4]

data = "&serverhostname=" + escape(sys.argv[6]) + "&fqdn=" + escape(sys.argv[7]) + "&techarea=" + escape(sys.argv[8]) + "&hostip=" + escape(sys.argv[9]) + "&hostmac=" + escape(sys.argv[10]) + "&webordatabase=" + escape(sys.argv[11]) + "&webdatabasesite=" + escape(sys.argv[12]) + "&webdatabaseinstance=" + escape(sys.argv[13]) + "&assettype=" + escape(sys.argv[14]) + "&machinerole=" + escape(sys.argv[15]) + "&tagList=" + escape(sys.argv[16])


# Assign the request headers for this particular API
headers = CaseInsensitiveDict() # Does not change
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[5]
headers["Content-Type"] = "application/x-www-form-urlencoded"

# Make the API request
resp = requests.put(url, headers=headers, data=json.dumps(data))

# print to the screen the status code (i.e. 200, 400, 404, etc)
print(resp.status_code)
print(resp.text)