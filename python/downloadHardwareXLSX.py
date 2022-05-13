# download the system package hardware listing to an XLSX file
# ex: python3 downloadHardwareXLSX.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxx

import sys
import requests
from requests.structures import CaseInsensitiveDict
import os

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/hardware/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)
filename = sys.argv[2] + "-HardwareListing.xlsx"
filepath = './download/'
file_path = os.path.join(filepath, filename)
r = requests.get(url, headers=headers, stream=True)
if r.ok:
  print("saving to", os.path.abspath(file_path))
  with open(file_path, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024 * 8):
      if chunk:
        f.write(chunk)
        f.flush()
        os.fsync(f.fileno())
else:  # HTTP status code 4XX/5XX
  print("Download failed: status code {}\n{}".format(r.status_code, r.text))

print(resp.status_code)
print("Request Completed")