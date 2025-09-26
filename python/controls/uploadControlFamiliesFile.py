# Upload a Control Families file
# API call from Developer's Guide: /api/external/controls/family/?applicationKey={applicationKey}
# ex: python3 uploadControlFamiliesFile.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx ./controlFamiliesUpload.xlsx

import sys
import requests
from requests.structures import CaseInsensitiveDict
import os

if len(sys.argv) < 4:
    print("Usage: python3 uploadControlFamiliesFile.py <URL> <applicationKey> <token> <filePath>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
file_path = sys.argv[4]

endpoint = "/api/external/controls/family/"
url = f"{base_url}{endpoint}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
    sys.exit(1)

try:
    with open(file_path, 'rb') as f:
        files = {'controlFamiliesFile': (os.path.basename(file_path), f, 'application/octet-stream')}

        resp = requests.post(url, headers=headers, files=files)
        
        print(f"HTTP Status Code: {resp.status_code}")
        if resp.status_code == 200:
            print(f"Control Families file {os.path.basename(file_path)} uploaded successfully.")
        else:
            print("Error uploading Control Families file:")
            print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")