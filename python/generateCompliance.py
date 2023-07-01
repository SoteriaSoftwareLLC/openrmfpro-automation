# Generate a new Compliance against statements, checklists, inheritance
# make sure the user is the system owner of the package
# ex: python3 generateCompliance.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxx "Latest Compliance with updated scand Feb 2023" "Our latest compliance scans from the most recent SCAP scans run across the network"

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/compliance/?applicationKey=" + sys.argv[3]
data = "title=" + sys.argv[5].replace(" ", "+") + "&description=" + sys.argv[6].replace(" ", "+")

# Assign the request headers for this particular API
headers = CaseInsensitiveDict() # Does not change
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]
headers["Content-Type"] = "application/x-www-form-urlencoded"

# Make the API request
resp = requests.post(url, headers=headers, data=data)

# print to the screen the status code (i.e. 200, 400, 404, etc)
print(resp.status_code)
print(resp.text)