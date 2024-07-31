#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables
import html

url = myVariables.rootURL + "/api/external/systempackage/machina-biometric/hardware/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken
# call the API
resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# make into a PrettyTable
hardwareTable = PrettyTable(["Title", "Key", "Hostname"])
# Just get the fields want
for element in json_object:  # iterate on each element of the list
    hardwareTable.add_row([element['systemTitle'], element['systemKey'], "<a href='getSystemPackageHardwareRecord.py?systemKey=" + element['systemKey'] +  "&hardwareid=" + element['internalIdString'] + "'>" + element['hostname'] + "</a>"])
# call to make this an HTML table and put into a new variable
htmlCode = hardwareTable.get_html_string(attributes={"class":"table"}, format=True)
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