#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables

url = myVariables.rootURL + "/api/external/systempackage/machina-biometric/software/65f9c7127e07c68d17e0a20f/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# print(json.dumps(json_object, indent=1))

RecordTable = PrettyTable(["Title", "Key", "Host Name", "Version", "Software Name"])
RecordTable.add_row([json_object['systemTitle'], json_object['systemKey'], json_object['hostName'], json_object['softwareName']])
    
# call to make this an HTML table and put into a new variable
htmlCode = RecordTable.get_html_string(attributes={"class":"table"}, format=True)

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