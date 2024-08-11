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

url = myVariables.rootURL + "/api/external/systempackage/" + str(arguments["systemKey"][0]) + "/teamsubpackage/items/?applicationKey=" + myVariables.applicationKey + "&teamKey=" + str(arguments["teamKey"][0])

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)

subpackagesTable = PrettyTable(["Title", "Team Key", "Item Type", "Item Name", "Description"])
itemList = json_object['data']
for element in itemList:  # iterate on each element of the list
    subpackagesTable.add_row([element['title'], element['teamKey'], element['itemTypeString'], element['itemName'], element['description']])
# call to make this an HTML table and put into a new variable
htmlCode = subpackagesTable.get_html_string(attributes={"class":"table"}, format=True)

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