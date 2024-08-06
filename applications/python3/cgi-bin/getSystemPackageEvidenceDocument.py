#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import html
import myVariables
import os
import urllib.parse

## get the query string. this gets passed to cgi scripts as the environment
## variable QUERY_STRING
query_string = os.environ['QUERY_STRING']

## convert the query string to a dictionary
arguments = urllib.parse.parse_qs(query_string)

url = myVariables.rootURL + "/api/external/systempackage/" + str(arguments["systemKey"][0]) + "/evidence/" + str(arguments["evidenceid"][0]) + "/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# print(json.dumps(json_object, indent=1))

evidenceTable = PrettyTable(["Evidence Id", "Title", "Description", "File Size", "Evidence Type", "File Type"])
evidenceTable.add_row([json_object['internalIdString'], json_object['title'], json_object['description'], json_object['fileSize'], json_object['evidenceTypeString'], json_object['fileTypeString']])

# call to make this an HTML table and put into a new variable
htmlCode = evidenceTable.get_html_string(attributes={"class":"table"}, format=True)
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