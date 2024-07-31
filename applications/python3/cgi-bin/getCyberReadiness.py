#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables

url = myVariables.rootURL + "/api/external/systempackage/machina-biometric/readinessscore/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
element = json.loads(resp.text)

cyberTable = PrettyTable(["Title", "Key", "Checklist Cyber Readiness", "Checklist Cat1 Open", "Number Of Checklists", "Patch Cyber Readiness", "Patch Critical Open", "Patch High Open", "Number Of Devices"])

cyberTable.add_row([element['systemTitle'], element['systemKey'], element['totalChecklistCyberReadiness'], element['numberOfChecklists'], element['totalChecklistCat1Open'], element['totalPatchCyberReadiness'], element['totalPatchCriticalOpen'], element['totalPatchHighOpen'], element['numberOfDevices']])
# call to make this an HTML table and put into a new variable
htmlCode = cyberTable.get_html_string(attributes={"class":"table"}, format=True)

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