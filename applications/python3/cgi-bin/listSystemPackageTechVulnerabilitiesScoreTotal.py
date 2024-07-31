#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables

url = myVariables.rootURL + "/api/external/systempackage/machina-biometric/techvulnerabilityscoretotal/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)

softwareTable = PrettyTable(["Title", "Key", "Version", "Closed", "False Positive", "Fixed", "Won't Fix", "Open", "Info", "Low", "Medium", "High", "Critical"])
 
softwareTable.add_row([json_object['systemTitle'], json_object['systemKey'], json_object['version'], json_object['totalClosed'], json_object['totalFalsePositive'], json_object['totalFixed'], json_object['totalWontFix'], json_object['totalOpen'], json_object['totalInfo'], json_object['totalLow'], json_object['totalMedium'], json_object['totalHigh'], json_object['totalCritical']])

# call to make this an HTML table and put into a new variable
htmlCode = softwareTable.get_html_string(attributes={"class":"table"}, format=True)

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
    