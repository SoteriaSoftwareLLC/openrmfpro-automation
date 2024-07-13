#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables

url = myVariables.rootURL + "/api/external/systempackage/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)

softwareTable = PrettyTable(["Title", "Key", "Host Name", "File Name"])
# Just get the fields want
for element in json_object: 
    softwareTable.add_row([element['systemTitle'], element['systemKey'], element['hostname'], element['filename']])
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
"title=" + sys.argv[4].replace(" ", "+") + "&systemKey=" + sys.argv[5] + "&description=" + sys.argv[6].replace(" ", "+") + "&confidentiality=" + sys.argv[7] + "&integrity=" + sys.argv[8] + "&availability=" + sys.argv[9] + "&packageType=" + sys.argv[10] + "&systemType=" + sys.argv[11].replace(" ", "+") + "&pocName=" + sys.argv[12].replace(" ", "+") + "&pocPhone=" + sys.argv[13].replace(" ", "+") + "&pocEmail=" + sys.argv[14] + "&addUserToSystemPackage=true&acronym=" + sys.argv[15].replace(" ", "+")