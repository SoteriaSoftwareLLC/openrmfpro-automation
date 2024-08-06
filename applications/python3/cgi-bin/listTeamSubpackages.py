#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables
import html

# set the URL with the 3 variables
url = myVariables.rootURL + "/api/external/teamsubpackages/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

# call the API
resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# make into a PrettyTable
systemPackageTable = PrettyTable(["System Package", "Key"])
# Just get the fields we want
for element in json_object:  # iterate on each element of the list
    systemPackageTable.add_row([element['title'], element['systemKey']])
# call to make this an HTML table and put into a new variable
htmlCode = systemPackageTable.get_html_string(attributes={"class":"table"}, format=True)
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