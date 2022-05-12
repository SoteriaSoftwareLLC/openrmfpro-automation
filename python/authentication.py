import sys
# Test the authentication and application key / token combination
# ex: python3 uploadSystemPackageSCAP.py http://192.168.13.111:8080 hvs.xxxxxxxxxxxxxxxx openrmfprosvc

import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/testauthentication"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Authorization"] = "Bearer " + sys.argv[2]
data = "applicationKey=" + sys.argv[3]

resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)