#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables
import html

url = myVariables.rootURL + "/api/external/systempackage/machina-biometric/software/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)

softwareTable = PrettyTable(["Title", "Key", "Host Name", "Software"])
# Just get the fields want
for element in json_object: 
    softwareTable.add_row([element['systemTitle'], element['systemKey'], element['hostname'], "<a href='getSystemPackageSoftwareRecord.py?systemKey=" + element['systemKey'] +  "&softwareid=" + element['internalIdString'] + "'>" + element['softwareName'] + "</a>"])
# call to make this an HTML table and put into a new variable
htmlCode = softwareTable.get_html_string(attributes={"class":"table"}, format=True)
# make the URL strings an actual URL
htmlCode = html.unescape(htmlCode)

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