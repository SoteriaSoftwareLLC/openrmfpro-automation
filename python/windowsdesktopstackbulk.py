# create a bunch of checklists based on templates for a particular hostname, also generated
# used for performance testing or loading a BUNCH of checklists for a templated deployment of workstations, servers, etc.
# ex: python3 windowsdesktopstackbulk.py http://192.168.13.111:8080 infradesktop openrmfprosvc hvs.xxxxxxxxx "6332e5b90e0b5d50d941738c,6332e5f60e0b5d50d941738f,6332e5a40e0b5d50d941738b,6332e5c90e0b5d50d941738d,6332e5db0e0b5d50d941738e" SOTWKS00  1 200

import sys
import requests
from requests.structures import CaseInsensitiveDict
import time

# Assign the API variables that are needed within the request's URL
TemplateIds=sys.argv[5]
checklistHostname=sys.argv[6]

# Build the API URL in order to make the request
url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/bulkadd/?applicationKey=" + sys.argv[3]

# Assign the request headers for this particular API
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Authorization"] = "Bearer " + sys.argv[4]
data = "templateIds="+TemplateIds

print ("----------------------------")
counter = int(sys.argv[7])
while counter <= int(sys.argv[8]):
    print("Making " +str(counter).zfill(5))
    # Make the API request
    resp = requests.post(url, headers=headers, data=data+"&checklistHostname="+checklistHostname+str(counter).zfill(5))
    # print to the screen the status code (i.e. 200, 400, 404, etc)
    print(resp.status_code)
    #print(resp.json)
    print(resp.text)
    time.sleep(200/1000)
    counter += 1

print ("----------------------------")