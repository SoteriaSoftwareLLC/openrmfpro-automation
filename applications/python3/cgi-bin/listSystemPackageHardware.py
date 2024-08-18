#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables
import html
import os
import urllib.parse

## get the query string. this gets passed to cgi scripts as the environment
## variable QUERY_STRING
query_string = os.environ['QUERY_STRING']

## convert the query string to a dictionary
arguments = urllib.parse.parse_qs(query_string)

url = myVariables.rootURL + "/api/external/systempackage/" + str(arguments["systemKey"][0]) + "/hardware/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken
# call the API
resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# make into a PrettyTable
hardwareTable = PrettyTable(["HostName", "Operating System", "Virtual?", "Patch Scan?", "Checklist?", "Tags"])
# Just get the fields want
for element in json_object:  # iterate on each element of the list
    hardwareTable.add_row(["<a href='getSystemPackageHardwareRecord.py?systemKey=" + element['systemKey'] + "&hardwareid=" + element['internalIdString'] + "&hostname=" + str(element['hostname']) + "'>" + str(element['hostname']) + "</a>", str(element['operatingSystem']), str(element['virtualServer']), str(element['patchscan']), str(element['checklist']), element['tags']])
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