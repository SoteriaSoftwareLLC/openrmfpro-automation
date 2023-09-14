# make a call to Keycloak to list system package groups
# main URL + /auth/admin/realms/openrmfpro/groups?search=machinabio_SystemOwner
# ex: python3 getUsers.py http://192.168.13.65:8080 token

import sys
import json
from prettytable import PrettyTable 
import requests
from requests.structures import CaseInsensitiveDict

# Create main System Package record
####################################################################################
url = sys.argv[1] + "/auth/admin/realms/openrmfpro/users" # or ?search=" + sys.argv[3]

# Assign the request headers for this particular API
headers = CaseInsensitiveDict() # Does not change
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[2]

# Make the API request
resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# print(json.dumps(json_object, indent=1))

# print the table of information
userTable = PrettyTable(["User Id", "Username", "User Email"])

for element in json_object:  # iterate on each element of the list for Id and Name
    userId = element['id'] 
    userName = element['username'] 
    userEmail = element['email']
    userTable.add_row([userId, userName, userEmail])

print(userTable)