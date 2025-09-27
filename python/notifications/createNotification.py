# create a notification
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/notification/?applicationKey={applicationKey}
# ex: python3 createNotification.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork "High Severity Alert" "A new Critical vulnerability was found on a key server."

import sys
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 7:
    print("Usage: python3 createNotification.py <URL> <applicationKey> <token> <systemKey> <title> <message>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
title = sys.argv[5]
message = sys.argv[6]
notification_type = sys.argv[7]

data = {
    "title": title,
    "message": message,
    "notificationType": notification_type,
}

endpoint = "/api/external/systempackage/{systemKey}/notification/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key)}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.post(url, headers=headers, data=data)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print("Notification created successfully.")
    else:
        print("Error creating Notification:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")