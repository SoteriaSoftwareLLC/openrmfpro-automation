#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables

url = myVariables.rootURL + "/api/external/systempackage/machina-biometric/checklistrecord/65f9c7d77e07c68d17e0a210/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# print(json.dumps(json_object, indent=1))

RecordTable = PrettyTable(["Title", "Key", "Host Name", "Version", "Open", "Not Applicable", "Not A Finding", "Not Reviewd", "Cat 1", "Cat 2", "Cat 3"])
RecordTable.add_row([json_object['systemTitle'], json_object['systemKey'], json_object['hostName'], json_object['version'], json_object['totalOpen'], json_object['totalNotApplicable'], json_object['totalNotAFinding'], json_object['totalNotReviewed'], json_object['totalCat1'], json_object['totalCat2'], json_object['totalCat3']])
    
# call to make this an HTML table and put into a new variable
htmlCode = RecordTable.get_html_string(attributes={"class":"table"}, format=True)

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