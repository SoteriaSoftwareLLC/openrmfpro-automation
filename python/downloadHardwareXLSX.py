import requests
from requests.structures import CaseInsensitiveDict
import os

url = "http://192.168.13.114:8080/api/external/systempackage/degthatnetwork/hardware/?applicationKey=degthatuploader"

headers = CaseInsensitiveDict()

headers["Accept"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

headers["Authorization"] = "Bearer s.Fl0KfrDNJwa2OHlt3RoFbF84"
resp = requests.get(url, headers=headers)
filename = "Hardware.xlsx"
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