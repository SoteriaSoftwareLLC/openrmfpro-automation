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

url = myVariables.rootURL + "/api/external/systempackage/" + str(arguments["systemKey"][0]) +"/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# print(json.dumps(json_object, indent=1))

recordTable = PrettyTable(["Title", "Key", "Package Type", "Number Of Checklists"])
recordTable.add_row([json_object['title'], json_object['systemKey'], json_object['packageTypeString'], json_object['numberOfChecklists']])
    
# call to make this an HTML table and put into a new variable
htmlCode = recordTable.get_html_string(attributes={"class":"table"}, format=True)
# make the URL strings an actual URL
htmlCode = html.unescape(htmlCode)
# make the links off the system package record here from the systemKey in the JSON object above
htmlMenu = "<p><a href='getSystemPackagePatchScore.py?systemKey=" + json_object['systemKey'] + "'>Patch Score</a><br />"
htmlMenu += "<a href='getSystemPackageChecklistScore.py?systemKey=" + json_object['systemKey'] + "'>Checklist Score</a><br />"
htmlMenu += "<a href='listSystemPackageChecklists.py?systemKey=" + json_object['systemKey'] + "'>List Checklists</a><br />"
htmlMenu += "<a href='listSystemPackageHardware.py?systemKey=" + json_object['systemKey'] + "'>List Hardware</a><br />"
htmlMenu += "<a href='listSystemPackageSoftware.py?systemKey=" + json_object['systemKey'] + "'>List Software</a><br />"
htmlMenu += "<a href='listSystemPackagePPSM.py?systemKey=" + json_object['systemKey'] + "'>List Ports/Protocols/Services</a><br />"
htmlMenu += "<a href='listSystemPackagePOAM.py?systemKey=" + json_object['systemKey'] + "'>List POAM</a><br />"
htmlMenu += "<a href='getCyberReadiness.py?systemKey=" + json_object['systemKey'] + "'>Get Cyber Readiness</a><br />"
htmlMenu += "<a href='listSystemPackageEvidence.py?systemKey=" + json_object['systemKey'] + "'>List Evidence</a><br />"
htmlMenu += "<a href='listSystemPackageComplianceListing.py?systemKey=" + json_object['systemKey'] + "'>List Compliance</a><br />"
htmlMenu += "<a href='listSystemPackageComplianceOverlays.py?systemKey=" + json_object['systemKey'] + "'>List Compliance Overlays</a><br />"
htmlMenu += "<a href='listSystemPackageMilestoneEvents.py?systemKey=" + json_object['systemKey'] + "'>List Milestones</a><br />"
htmlMenu += "<a href='listSystemPackageMitigationStatements.py?systemKey=" + json_object['systemKey'] + "'>List Mitigation Statements</a><br />"
htmlMenu += "<a href='getListOfTeamSubpackages.py?systemKey=" + json_object['systemKey'] + "'>List Team Subpackages</a><br />"
htmlMenu += "<a href='listNotifications.py?systemKey=" + json_object['systemKey'] + "'>List Notifications</a><br />"
htmlMenu += "<a href='listSystemPackagePatchVulnerabilities.py?systemKey=" + json_object['systemKey'] + "'>List Patch Vulnerabilities</a><br />"
htmlMenu += "<a href='listSystemPackagePatchScoreForDeviceListing.py?systemKey=" + json_object['systemKey'] + "'>List Patch Score By Device Listing</a><br />"
htmlMenu += "<a href='listSystemPackageTechVulnerabilitiesSoftware.py?systemKey=" + json_object['systemKey'] + "'>List Tech Vulnerabilities (Software)</a><br />"
htmlMenu += "<a href='listSystemPackageTechVulnerabilitiesContainer.py?systemKey=" + json_object['systemKey'] + "'>List Tech Vulnerabilities (Container)</a><br />"
htmlMenu += "<a href='listSystemPackageTechVulnerabilitiesLog.py?systemKey=" + json_object['systemKey'] + "'>List Tech Vulnerabilities (Log)</a><br />"
htmlMenu += "<a href='listSystemPackageTechVulnerabilitiesOther.py?systemKey=" + json_object['systemKey'] + "'>List Tech Vulnerabilities (Other)</a><br />"
htmlMenu += "<a href='listSystemPackageTechVulnerabilitiesTotalScore.py?systemKey=" + json_object['systemKey'] + "'>List Tech Vulnerabilities Total Score</a><br />"
htmlMenu += "</p>"
# unescape them
htmlMenu = html.unescape(htmlMenu)

# print out the HTML fully page
print(
"""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<body>"""
)
print(htmlCode)
print(htmlMenu)
print(
"""\
</body>
</html>"""
)