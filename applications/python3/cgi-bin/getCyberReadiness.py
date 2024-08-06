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

url = myVariables.rootURL + "/api/external/systempackage/" + str(arguments["systemKey"][0]) + "/readinessscore/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
element = json.loads(resp.text)

cyberTable = PrettyTable(["Checklist Cyber Readiness", "Checklist Cat1 Open", "Number Of Checklists", "Patch Cyber Readiness", "Patch Critical Open", "Patch High Open", "Number Of Devices", "Tech Cyber Readiness", "Tech Critical Open", "Tech High Open", "Number of Projects"])

cyberTable.add_row([element['totalChecklistCyberReadiness'], element['totalChecklistCat1Open'], element['numberOfChecklists'], element['totalPatchCyberReadiness'], element['totalPatchCriticalOpen'], element['totalPatchHighOpen'], element['numberOfDevices'], element['totalTechnologyCyberReadiness'], element['totalTechCriticalOpen'], element['totalTechHighOpen'], element['numberOfProjects']])
# call to make this an HTML table and put into a new variable
htmlCode = cyberTable.get_html_string(attributes={"class":"table"}, format=True)

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