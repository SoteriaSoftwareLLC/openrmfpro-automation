# get a system package record and all scores
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/?applicationKey={applicationKey}
# ex: python3 downloadAllSystemPackageChecklists.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import json
from prettytable import PrettyTable 
import requests
from requests.structures import CaseInsensitiveDict

import sys
import json
import requests
from prettytable import PrettyTable 
from requests.structures import CaseInsensitiveDict

def clean_up_filenames(string):
    return "-".join(string.split()).replace("/","-")

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(json.dumps(json_object, indent=1))
sp_json_object = json.loads(resp.text)

# get the numberOfChecklists from sp_json_object

checklistNumbersTable = PrettyTable(["Number of Checklists"])
totalChecklistNumber = sp_json_object["numberOfChecklists"]
checklistNumbersTable.add_row([totalChecklistNumber])
print(checklistNumbersTable)

# cycle through all checklists one at a time max 50, then repeat
# set the total checklistNumber
totalChecklistNumber = 0
# set the max to pull down
maxChecklistsToReturn = 50
# current page of the results, starting with page 1
currentChecklistResultsPage = 1
# format type ckl or cklb
checklistFormat = "cklb"
# directory from the current path to create for all the checklist download files
checklistDirectory = "download"

while True:
    if totalChecklistNumber > ((currentChecklistResultsPage+1)*maxChecklistsToReturn):
        break
    url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/checklists/?applicationKey=" + sys.argv[3] + "&page=" + str(currentChecklistResultsPage) + "&limit=" + str(maxChecklistsToReturn)
    # print(url)
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer " + sys.argv[4]
    resp = requests.get(url, headers=headers)

    checklist_listing_json_object = json.loads(resp.text)
    # print(json.dumps(checklist_listing_json_object, indent=1))
    checklistListTable = PrettyTable(["Checklist Id", "Checklist File"])
    if not checklist_listing_json_object:
        break # exit out no more data
    for element in checklist_listing_json_object:
        if not element['artifactId']:
            break # exit out a bad record possibly
        checklistId = element['artifactId']
        checklistFullTitle = clean_up_filenames(element['artifactTitle'])
        checklistListTable.add_row([checklistId, checklistFullTitle])
        # download the file
        downloadUrl = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/checklist/" + checklistId + "/?format=" + checklistFormat + "&applicationKey=" + sys.argv[3]
        # print(downloadUrl)
        downloadHeaders = CaseInsensitiveDict()
        downloadHeaders["Accept"] = "application/xml;charset=utf-8"
        downloadHeaders["Authorization"] = "Bearer " + sys.argv[4]
        downloadResp = requests.get(downloadUrl, headers=downloadHeaders)
        with open(checklistDirectory + "/" + checklistFullTitle + ".ckl", "w") as downloadFile:
            print(downloadResp.text, file=downloadFile)

    currentChecklistResultsPage += 1
    # print them all out, max 50
    print(checklistListTable)

print ("--------------")