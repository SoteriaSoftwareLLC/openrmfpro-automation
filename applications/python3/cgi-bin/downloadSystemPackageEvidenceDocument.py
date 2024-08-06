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

url = myVariables.rootURL + "/api/external/systempackage/" + str(arguments["systemKey"][0]) + "/evidence/" + str(arguments["systemKey"][0]) + "/download/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken
# call the API
resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# make into a PrettyTable
evidenceTable = PrettyTable(["Internal Id", "Title","Evidence Type", "File Type"])
# Just get the fields want
for element in json_object:  # iterate on each element of the list
    evidenceTable.add_row([element['internalIdString'], element['title'], element['evidenceTypeString'], element['fileTypeString']])
# call to make this an HTML table and put into a new variable
htmlCode = evidenceTable.get_html_string(attributes={"class":"table"}, format=True)
htmlCode = html.unescape(htmlCode)

filename = json_object['filename']
contentType = json_object['contentType']

# now get the file with the valid content type
fileHeaders = CaseInsensitiveDict()
fileHeaders["Accept"] = contentType
fileHeaders["Authorization"] = "Bearer "+ myVariables.bearerToken
# open in binary mode
with open("../download/" + filename, "wb") as file:
    # get request
    response = requests.get(url, headers=fileHeaders)
    # write to file
    file.write(response.content)

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