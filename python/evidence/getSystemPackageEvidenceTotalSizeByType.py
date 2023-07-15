# list the system package Evidence records total file count and total file size, broken down by the 4 Evidence types
# General = 10, Checklist = 20, POAM = 30, Compliance Statement = 40
# ex: python3 getSystemPackageEvidenceTotalSizeByType.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/evidence/?general=true&checklist=true&statement=true&poam=true&applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

# store the total sizes and add it up
totalGeneralSize = 0
totalGeneralFiles = 0
totalChecklistSize = 0
totalChecklistFiles = 0
totalPOAMSize = 0
totalPOAMFiles = 0
totalComplianceSize = 0
totalComplianceFiles = 0

json_object = json.loads(resp.text)
for element in json_object:  # iterate on each element of the list
    if element['evidenceType'] == 10:
        totalGeneralSize = totalGeneralSize + element['fileSize'] # add to the going total
        totalGeneralFiles = totalGeneralFiles + 1
    elif element['evidenceType'] == 20:
        totalChecklistSize = totalChecklistSize + element['fileSize'] # add to the going total
        totalChecklistFiles = totalChecklistFiles + 1
    elif element['evidenceType'] == 30:
        totalPOAMSize = totalPOAMSize + element['fileSize'] # add to the going total
        totalPOAMFiles = totalPOAMFiles + 1
    elif element['evidenceType'] == 40:
        totalComplianceSize = totalComplianceSize + element['fileSize'] # add to the going total
        totalComplianceFiles = totalComplianceFiles + 1

print("------------------------------------")
print("General Evidence Files")
print("------------------------------------")
print("Total Files: " + str(totalGeneralFiles))  # print it
print("Total Size:  " + str(totalGeneralSize) + " KB")  # print it
print("------------------------------------")
print("Checklist Evidence Files")
print("------------------------------------")
print("Total Files: " + str(totalChecklistFiles))  # print it
print("Total Size:  " + str(totalChecklistSize) + " KB")  # print it
print("------------------------------------")
print("POAM Evidence Files")
print("------------------------------------")
print("Total Files: " + str(totalPOAMFiles))  # print it
print("Total Size:  " + str(totalPOAMSize) + " KB")  # print it
print("------------------------------------")
print("Compliance Statement Evidence Files")
print("------------------------------------")
print("Total Files: " + str(totalComplianceFiles))  # print it
print("Total Size:  " + str(totalComplianceSize) + " KB")  # print it
print("------------------------------------")