#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables

url = myVariables.rootURL + "/api/external/systempackage/machina-biometric/checklists/?applicationKey=" + myVariables.applicationKey + "&page=1&limit=50"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

# call the API
resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# make into a PrettyTable
checklistsTable = PrettyTable(["Host Name", "Type", "Version", "Release", "Open", "Not Applicable", "Not A Finding", "Not Reviewed", "Cat1", "Cat2", "Cat3", "Updated"])
# Just get the fields want
for element in json_object:  # iterate on each element of the list
    checklistsTable.add_row([element['hostName'], "<a href='getSystemPackageRecord.py?systemKey=" + element['systemKey'] + "&checklistid=" + element['internalIdString'] + "'>" + element['stigType'] + "</a>", element['stigVersion'], element['stigRelease'], element['totalOpen'], element['totalNotApplicable'], element['totalNotAFinding'], element['totalNotReviewed'], element['totalCat1'], element['totalCat2'], element['totalCat3'], element['updatedDateString']])
# call to make this an HTML table and put into a new variable
htmlCode = checklistsTable.get_html_string(attributes={"class":"table"}, format=True)

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