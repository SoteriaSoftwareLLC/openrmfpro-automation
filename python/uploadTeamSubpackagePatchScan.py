# Upload Nessus patch scan results *.nessus file
# ex: python3 uploadSystemPackageSCAP.py http://192.168.13.111:8080 companyinfra network team openrmfprosvc hvs.xxxxxxxxxxxxxxxx ../data/scap-scans/ DEGTHAT_SCC-5.0.1_2019-04-19_170849_XCCDF-Results_Microsoft_Outlook_2016-001.003.xml

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/teamsubpackage/" + sys.argv[3] + "/patchscan/?applicationKey=" + sys.argv[4]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[5]

# file name of file to be uploaded hosted locally in the same directory as the python code
with open(sys.argv[6] + sys.argv[7], "rb") as a_file:
    patchscanFile = {sys.argv[7] : a_file}
    resp = requests.post(url, headers=headers, files=patchscanFile)

print(resp.status_code)
print(resp.text)