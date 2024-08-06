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

url = myVariables.rootURL + "/api/external/templaterecord/" + str(arguments["templateid"][0]) + "/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# print(json.dumps(json_object, indent=1))

recordTable = PrettyTable(["Internal Id", "Title", "Template Type", "Version", "Open", "Not Applicable", "Not A Finding", "Not Reviewed", "Cat 1", "Cat 2", "Cat 3"]) 
recordTable.add_row([json_object['internalIdString'], json_object['title'], json_object['templateTypeString'], json_object['version'], str(json_object['score']['totalOpen']), str(json_object['score']['totalNotApplicable']), str(json_object['score']['totalNotAFinding']), str(json_object['score']['totalNotReviewed']), str(json_object['score']['totalCat1']), str(json_object['score']['totalCat2']), str(json_object['score']['totalCat3'])])
    
# call to make this an HTML table and put into a new variable
htmlCode = recordTable.get_html_string(attributes={"class":"table"}, format=True)

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