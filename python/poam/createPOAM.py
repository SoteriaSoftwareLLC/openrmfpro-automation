# Create a POAM in the system package
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/poam/?applicationKey={applicationKey}
# ex: python3 createPOAM.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxx 

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/poam/?applicationKey=" + sys.argv[3]

# Assign the request headers for this particular API
headers = CaseInsensitiveDict() # Does not change
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

# Make the API request
resp = requests.post(url, headers=headers)

# print to the screen the status code (i.e. 200, 400, 404, etc)
print(resp.status_code)
print(resp.text)