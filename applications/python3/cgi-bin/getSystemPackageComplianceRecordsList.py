#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables

url = myVariables.rootURL + "/api/external/systempackage/machina-biometric/compliance/65f9c7e17e07c68d17e0a237/records/?applicationKey=" + myVariables.applicationKey + "&page=1&limit=50"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# print(json.dumps(json_object, indent=1))

recordListTable = PrettyTable(["Compliance Id", "System Title", "Key", "Title"])

for element in json_object:  # iterate on each element of the list
    recordListTable.add_row([element['systemComplianceId'], element['systemTitle'], element['systemKey'], element['title']])
# call to make this an HTML table and put into a new variable
htmlCode = recordListTable.get_html_string(attributes={"class":"table"}, format=True)
    
# call to make this an HTML table and put into a new variable
htmlCode = recordListTable.get_html_string(attributes={"class":"table"}, format=True)

# print out the HTML fully page
print(
"""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<body>"""
)
print(htmlCode)
print(
"""\
</body>
</html>"""
)