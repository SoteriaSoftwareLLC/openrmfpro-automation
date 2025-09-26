# update the system package preferences
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/preferences/?applicationKey={applicationKey}
# ex: python3 updateSystemPackagePreferences.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork "My Title" "My Description" true true true "My Classification" "My Classification Color"

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 11:
    print("Usage: python3 updateSystemPackagePreferences.py <URL> <applicationKey> <token> <systemKey> <title> <description> <allowUncredentialedScans> <allowSeverityOverride> <ipMasking> <classification> <classificationColor>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
title = sys.argv[5]
description = sys.argv[6]
allow_uncredentialed_scans = sys.argv[7]
allow_severity_override = sys.argv[8]
ip_masking = sys.argv[9]
classification = sys.argv[10]
classification_color = sys.argv[11]

data = {
    "title": title,
    "description": description,
    "allowUncredentialedScans": allow_uncredentialed_scans,
    "allowSeverityOverride": allow_severity_override,
    "ipMasking": ip_masking,
    "classification": classification,
    "classificationColor": classification_color,
}

endpoint = "/api/external/systempackage/{systemKey}/preferences/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.put(url, headers=headers, data=data)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print("System Package preferences updated successfully.")
    else:
        print("Error updating preferences:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")