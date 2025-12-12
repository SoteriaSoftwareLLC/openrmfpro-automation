# Upload a list of *.xml files from DISA cyber.mil of the checklist templates to create new checklist templates in OpenRMF Professional
# make sure you have the TemplateAdministrator Role for the user associated with the token you are using

# ex: python3 bulkUploadNewDISAChecklistTemplates.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxx <full-path-to-directory>

import sys
import requests
import os
import glob
from requests.structures import CaseInsensitiveDict

# Check if we have enough arguments
if len(sys.argv) < 5:
    print("Usage: python3 bulkUploadNewDISAChecklistTemplates.py <url> <app_key> <token> <directory_path_to_files>")
    sys.exit(1)

####################################################################################
# Mitigation Statements Upload from XLSX files
####################################################################################
print("Adding DISA Checklist Template XML files")
number_of_files_uploaded = 0

url = sys.argv[1] + "/api/external/template/disa/?applicationKey=" + sys.argv[2]
headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer " + sys.argv[3]
print("Uploading files in " + sys.argv[4] + "/*.xml")

for file in glob.glob(sys.argv[4] + '/*.xml', recursive=False):
    with open(file, "rb") as a_file:
        templateFile = {file : a_file}
        resp = requests.post(url, headers=headers, files=templateFile)
        number_of_files_uploaded += 1
        print(str(resp.status_code) + " Checklist Template File " + os.path.basename(file) + " uploaded")

####################################################################################
# Done
####################################################################################
print("Completed uploading all " + str(number_of_files_uploaded) + " files")