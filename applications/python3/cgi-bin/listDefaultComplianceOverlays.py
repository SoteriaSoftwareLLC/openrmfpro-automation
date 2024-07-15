#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables

url = myVariables.rootURL + "/api/external/overlay/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken
# call the API
resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# make into a PrettyTable
overlayTable = PrettyTable(["Internal Id", "Title", "Number Of Controls", "Manually Added"])
# Just get the fields want
for element in json_object:  # iterate on each element of the list
    overlayTable.add_row([element['internalIdString'], element['title'], element['numberOfControls'], element['manuallyAdded']])
# call to make this an HTML table and put into a new variable
htmlCode = overlayTable.get_html_string(attributes={"class":"table"}, format=True)

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