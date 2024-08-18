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

url = myVariables.rootURL + "/api/external/systempackage/" + str(arguments["systemKey"][0]) + "/hardware/" + str(arguments["hardwareid"][0]) + "/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# print(json.dumps(json_object, indent=1))

recordTable = PrettyTable(["Title", "Key", "Host Name", "Internal Id"])    
recordTable.add_row([json_object['systemTitle'], json_object['systemKey'], json_object['hostname'], json_object['internalIdString']])
# call to make this an HTML table and put into a new variable
htmlCode = recordTable.get_html_string(attributes={"class":"table"}, format=True)

htmlCode = html.unescape(htmlCode)

## get the hardware device score

urlScore = myVariables.rootURL + "/api/external/systempackage/" + str(arguments["systemKey"][0]) + "/patchscore/device/" + str(arguments["hostname"][0]) + "/?applicationKey=" + myVariables.applicationKey

respScore = requests.get(urlScore, headers=headers)
json_objectScore = json.loads(respScore.text)

recordTableScore = PrettyTable(["Critical Open", "High Open", "Medium Open", "Low Open", "Info Open"])    
recordTableScore.add_row([json_objectScore['totalCriticalOpen'], json_objectScore['totalHighOpen'], json_objectScore['totalMediumOpen'], json_objectScore['totalLowOpen'], json_objectScore['totalInfoOpen']])
# call to make this an HTML table and put into a new variable
htmlCodeScore = recordTableScore.get_html_string(attributes={"class":"table"}, format=True)

htmlCodeScore = html.unescape(htmlCodeScore)

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
"""<br /><br />"""
)
print(htmlCodeScore)
print(
"""\
</body>
</html>"""
)