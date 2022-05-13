# list all the other tech vulnerabilities in a system package
# ex: python3 listSystemPackageTechVulnerabilities.py http://192.168.13.111:8080 companyinfra 10 openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/techvulnerabilitydata/?categoryType=" + sys.argv[3] + "&applicationKey=" + sys.argv[4]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[5]

resp = requests.get(url, headers=headers)
print(resp.status_code)
print(resp.text)