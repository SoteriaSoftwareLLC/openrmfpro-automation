# Add a brand new system package
# make sure you have the SystemPackageAdministrator Role
# API call from Developer's Guide: /api/external/systempackage/?applicationKey={applicationKey}
# ex: python3 addSystemPackage.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxx 'Automated Infrastructure System Package' automatedinfra 'My automated system package for infrastructure done entirely via API calls' 20 20 20 10 'Infrastructure ATO' 'Dale Bingham' '855-RMF-0848' 'support@soteriasoft.com' 'AUTOINFRA'

# For the packageType use the following:
# 10 = RMF (default) – requires the CIA levels
# 20 = FedRAMP – requires the FedRAMP Level

# For RMF Confidentiality, Integrity, and Availability and FedRAMP level:
# 10 = Low (default)
# 20 = Moderate
# 30 = High
# For FedRAMP LI-SaaS use 40

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/?applicationKey=" + sys.argv[2]

data = "title=" + sys.argv[4].replace(" ", "+") + "&systemKey=" + sys.argv[5] + "&description=" + sys.argv[6].replace(" ", "+") + "&confidentiality=" + sys.argv[7] + "&integrity=" + sys.argv[8] + "&availability=" + sys.argv[9] + "&packageType=" + sys.argv[10] + "&systemType=" + sys.argv[11].replace(" ", "+") + "&pocName=" + sys.argv[12].replace(" ", "+") + "&pocPhone=" + sys.argv[13].replace(" ", "+") + "&pocEmail=" + sys.argv[14] + "&addUserToSystemPackage=true&acronym=" + sys.argv[15].replace(" ", "+")

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