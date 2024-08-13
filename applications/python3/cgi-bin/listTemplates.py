#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables
import html

url = myVariables.rootURL + "/api/external/templates/disa/?applicationKey=" + myVariables.applicationKey + "&searchString="

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)

listTemplatesTable = PrettyTable(["Title", "STIG Version", "STIG Release"])

for element in json_object:  # iterate on each element of the list
    listTemplatesTable.add_row(["<a href='getTemplateChecklistRecord.py?templateid=" + element['internalIdString'] + "'>" + element['title'] + "</a>", element['stigVersion'], element['stigRelease']])

# call to make this an HTML table and put into a new variable
htmlCode = listTemplatesTable.get_html_string(attributes={"class":"table"}, format=True)
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