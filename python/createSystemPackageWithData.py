# Add a brand new system package and a bunch of data, generated POAM, and generated initial Compliance
# make sure you have the SystemPackageAdministrator Role
# the 5th parameter shown in the example below 'automatedinfra' is used as the system key throughout the rest of this script to load data
# ex: python3 createSystemPackageWithData.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxx 'Automated Infrastructure System Package' automatedinfra 'My automated system package for infrastructure done entirely via API calls' 20 20 20 10 'Infrastructure ATO' 'Dale Bingham' '855-RMF-0848' 'support@soteriasoft.com' 'AUTOINFRA'

# For the packageType use the following:
# 10 = RMF (default) – requires the CIA levels
# 20 = FedRAMP – requires the FedRAMP Level

# For RMF Confidentiality, Integrity, and Availability and FedRAMP level:
# 10 = Low (default)
# 20 = Moderate
# 30 = High
# For FedRAMP LI-SaaS use 40

# this pulls in files from checklist path and a patch scan single file as well as files from mitigation statements and compliance statements

import sys
import requests
import os
import glob
from requests.structures import CaseInsensitiveDict

####################################################################################
# Create main System Package record
####################################################################################
url = sys.argv[1] + "/api/external/systempackage/?applicationKey=" + sys.argv[2]

data = "title=" + sys.argv[4].replace(" ", "+") + "&systemKey=" + sys.argv[5] + "&description=" + sys.argv[6].replace(" ", "+") + "&confidentiality=" + sys.argv[7] + "&integrity=" + sys.argv[8] + "&availability=" + sys.argv[9] + "&packageType=" + sys.argv[10] + "&systemType=" + sys.argv[11].replace(" ", "+") + "&pocName=" + sys.argv[12].replace(" ", "+") + "&pocPhone=" + sys.argv[13].replace(" ", "+") + "&pocEmail=" + sys.argv[14] + "&addUserToSystemPackage=true&acronym=" + sys.argv[15].replace(" ", "+")

# Assign the request headers for this particular API
headers = CaseInsensitiveDict() # Does not change
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[3]
headers["Content-Type"] = "application/x-www-form-urlencoded"

# Make the API request
resp = requests.post(url, headers=headers, data=data)

# print to the screen the status code (i.e. 200, 400, 404, etc)
print(str(resp.status_code) + " System Package created")

####################################################################################
# Mitigation Statements Upload from XLSX files
####################################################################################
print("Adding Mitigation Statements")

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[5] + "/mitigationstatements/?applicationKey=" + sys.argv[2]
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[3]
for file in glob.glob('../data/Mitigations/*.xlsx', recursive=False):
    with open(file, "rb") as a_file:
        mitigationFile = {file : a_file}
        resp = requests.post(url, headers=headers, files=mitigationFile)

    print(str(resp.status_code) + " Migitation Statement " + os.path.basename(file) + " added")


####################################################################################
# Compliance Statements Upload from XLSX files
####################################################################################
print("Adding Compliance Statements")

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[5]+ "/compliancestatements/?applicationKey=" + sys.argv[2]
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[3]
for file in glob.glob('../data/ComplianceData/*.xlsx', recursive=False):
    with open(file, "rb") as a_file:
        mitigationFile = {file : a_file}
        resp = requests.post(url, headers=headers, files=mitigationFile)

    print(str(resp.status_code) + " Compliance Statement " + os.path.basename(file) + " added")

####################################################################################
# Upload Patch files in order
####################################################################################
print("Adding Patch Vulnerability Scans")

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[5]+ "/patchscan/?applicationKey=" + sys.argv[2]
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[3]

# file name of file to be uploaded hosted locally in the same directory as the python code
for file in glob.glob('../data/patch-vulnerability-scans/DEGTHAT-2023-Jan.nessus', recursive=False):
    with open(file, "rb") as a_file:
        patchscanFile = {file : a_file}
        resp = requests.post(url, headers=headers, files=patchscanFile)
        print(str(resp.status_code) + " Patch Scan " + os.path.basename(file) + " uploaded")
for file in glob.glob('../data/patch-vulnerability-scans/IDS-CONEX-HQ-2023-Jan.nessus', recursive=False):
    with open(file, "rb") as a_file:
        patchscanFile = {file : a_file}
        resp = requests.post(url, headers=headers, files=patchscanFile)
        print(str(resp.status_code) + " Patch Scan " + os.path.basename(file) + " uploaded")
for file in glob.glob('../data/patch-vulnerability-scans/DEGTHAT-2023-Mar.nessus', recursive=False):
    with open(file, "rb") as a_file:
        patchscanFile = {file : a_file}
        resp = requests.post(url, headers=headers, files=patchscanFile)
        print(str(resp.status_code) + " Patch Scan " + os.path.basename(file) + " uploaded")
for file in glob.glob('../data/patch-vulnerability-scans/IDS-CONEX-HQ-2023-Mar.nessus', recursive=False):
    with open(file, "rb") as a_file:
        patchscanFile = {file : a_file}
        resp = requests.post(url, headers=headers, files=patchscanFile)
        print(str(resp.status_code) + " Patch Scan " + os.path.basename(file) + " uploaded")
for file in glob.glob('../data/patch-vulnerability-scans/DEGTHAT-2023-May.nessus', recursive=False):
    with open(file, "rb") as a_file:
        patchscanFile = {file : a_file}
        resp = requests.post(url, headers=headers, files=patchscanFile)
        print(str(resp.status_code) + " Patch Scan " + os.path.basename(file) + " uploaded")
for file in glob.glob('../data/patch-vulnerability-scans/IDS-CONEX-HQ-2023-May.nessus', recursive=False):
    with open(file, "rb") as a_file:
        patchscanFile = {file : a_file}
        resp = requests.post(url, headers=headers, files=patchscanFile)
        print(str(resp.status_code) + " Patch Scan " + os.path.basename(file) + " uploaded")

####################################################################################
# Creating POAM
####################################################################################
print("Making POAM")

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[5]+ "/poam/?applicationKey=" + sys.argv[2]

# Assign the request headers for this particular API
headers = CaseInsensitiveDict() # Does not change
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[3]

# Make the API request
resp = requests.post(url, headers=headers)

# print to the screen the status code (i.e. 200, 400, 404, etc)
print(str(resp.status_code) + " creating POAM")

####################################################################################
# Upload Checklist files
####################################################################################
print("Adding Checklists")

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[5]+ "/scapchecklist/?applicationKey=" + sys.argv[2]
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[3]

# file name of checklist file to be uploaded hosted locally, passing in the directory name and filename
for file in glob.glob('../data/checklists/*.ckl', recursive=False):
    with open(file, "rb") as a_file:
        checklistFile = {file : a_file}
        resp = requests.post(url, headers=headers, files=checklistFile)
        print(str(resp.status_code) + " Checklist " + os.path.basename(file) + " uploaded")
# file name of SCAP result file to be uploaded hosted locally, passing in the directory name and filename
for file in glob.glob('../data/scap-scans/SoteriaWKS*.xml', recursive=False):
    with open(file, "rb") as a_file:
        checklistFile = {file : a_file}
        resp = requests.post(url, headers=headers, files=checklistFile)
        print(str(resp.status_code) + " SCAP scan result " + os.path.basename(file) + " uploaded")

####################################################################################
# Generate Compliance Listing Baseline
####################################################################################
print("Generating Compliance Baseline")

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[5]+ "/compliance/?applicationKey=" + sys.argv[2]
data = "title=Initial+Compliance+Baseline&description=Auto-generated+initial+compliance+baseline+from+setup"

# Assign the request headers for this particular API
headers = CaseInsensitiveDict() # Does not change
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[3]
headers["Content-Type"] = "application/x-www-form-urlencoded"

# Make the API request
resp = requests.post(url, headers=headers, data=data)

# print to the screen the status code (i.e. 200, 400, 404, etc)
print(str(resp.status_code) + " compliance listing generated from statements and checklists")

####################################################################################
# Done
####################################################################################
print("Completed setting up initial system package " + sys.argv[5])