# Upload a Framework Levels file
# API call from Developer's Guide: /api/external/controls/framework/levels/?applicationKey={applicationKey}
# ex: python3 uploadFrameworkLevelsFile.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx ./frameworkLevelsUpload.xlsx

import sys
import requests
from requests.structures import CaseInsensitiveDict
import os

if len(sys.argv) < 4:
    print("Usage: python3 uploadFrameworkLevelsFile.py <URL> <applicationKey> <token> <filePath>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
file_path = sys.argv[4]

endpoint = "/api/external/controls/framework/levels/"
url = f"{base_url}{endpoint}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
    sys.exit(1)

try:
    with open(file_path, 'rb') as f:
        files = {'frameworkLevelsFile': (os.path.basename(file_path), f, 'application/octet-stream')}

        resp = requests.post(url, headers=headers, files=files)
        
        print(f"HTTP Status Code: {resp.status_code}")
        if resp.status_code == 200:
            print(f"Framework Levels file {os.path.basename(file_path)} uploaded successfully.")
        else:
            print("Error uploading Framework Levels file:")
            print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")