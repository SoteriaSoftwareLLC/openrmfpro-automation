# Add a brand new system package
# ex: python3 authentication.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxx

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/testauthentication"
data = "applicationKey=" + sys.argv[2]

# Assign the request headers for this particular API
headers = CaseInsensitiveDict() # Does not change
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[3]
headers["Content-Type"] = "application/x-www-form-urlencoded"

# Make the API request
resp = requests.post(url, headers=headers, data=data)

# print to the screen the status code (i.e. 200, 400, 404, etc)
print(resp.status_code)
print(resp.text)