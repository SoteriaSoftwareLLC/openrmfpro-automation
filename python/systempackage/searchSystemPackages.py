# list system packages this user has access to at least view
# API call from Developer's Guide: /api/external/systempackages/?applicationKey={applicationKey}
# ex: python3 searchSystemPackages.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackages/?applicationKey=" + sys.argv[2]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[3]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
# print(json.dumps(json_object, indent=1))

for element in json_object:  # iterate on each element of the list
    title = element['title']  # get the title
    systemKey = element['systemKey']  # get the system key
    description = element['description']  # get the description
    numberOfChecklists = element['numberOfChecklists'] # get number of checklists
    pocEmail = element['pocEmail']  # get the pocEmail
    print("Title: " + title)  # print it
    print("System Key: " + systemKey)  # print it
    print("Description: " + description)  # print it
    print("Number of Checklists: " + str(numberOfChecklists)) # print it
    print("pocEmail: " + pocEmail)  # print it
    print("-----------------------")
