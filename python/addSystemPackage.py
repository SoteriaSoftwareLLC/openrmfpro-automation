# Add a brand new system package
# make sure you have the SystemPackageAdministrator Role
# ex: python3 addSystemPackage.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxx

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/?applicationKey=" + sys.argv[2]

APIname = "systempackage" # Constant for this particular API
AppKey = "applicationKey=degthatuploader"  # "degthatuploader is an example application key - replace it.
SystemKey = "degthatnetwork"
data = "title=MyPackage&systemKey=mykeywithlowercaseletters&description=This+is+my+description&confidentiality=10&integrity=10&availability=10&fedrampLevel=10&packageType=10&systemType=Business+System&pocName=My+First+and+Last&pocPhone=8003456789 &pocEmail=info@soteriasoft.com&addUserToSystemPackage=true&acronym=TBD"

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