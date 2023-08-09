# get the access token to use for subsequent calls
# main URL + /auth/realms/master/protocol/openid-connect/token
# content type application/x-www-form-urlencoded
# 4 fields posted
# client_id = admin-cli
# username
# password
# grant_type password

# ex: python3 getAuthToken.py http://192.168.13.65:8080 admin mypasswordgoeshere

import sys
import requests
import json
from requests.structures import CaseInsensitiveDict

# Create main System Package record
####################################################################################
url = sys.argv[1] + "/auth/realms/master/protocol/openid-connect/token"
data = "client_id=admin-cli&grant_type=password&username=" + sys.argv[2] + "&password=" + sys.argv[3]

# Assign the request headers for this particular API
headers = CaseInsensitiveDict() # Does not change
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/x-www-form-urlencoded"

# Make the API request
resp = requests.post(url, headers=headers, data=data)

json_object = json.loads(resp.text)
print(json_object["access_token"])
