# Add a brand new system package
# make sure you have the SystemPackageAdministrator Role
# API call from Developer's Guide: /api/external/systempackage/?applicationKey={applicationKey}
# ex: python3 addSystemPackage.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx MyTitle mykeywithlowercaseletters "My description" "My First and Last" 855-763-0848 info@soteriasoft.com true MYACRONYM 68bb00bb05c51ab74f106611c "68bb00b05c51ab74f1066129|68bb00b05c51ab74f106612c|68bb00b05c51ab74f1066131"

import sys
import requests
from requests.structures import CaseInsensitiveDict

MIN_ARGS = 13

if len(sys.argv) < MIN_ARGS:
    print("Usage: python3 addSystemPackage.py <URL> <applicationKey> <token> <title> <systemKey> <description> <pocName> <pocPhone> <pocEmail> <addUserToSystemPackage> <acronym> <frameworkId> <frameworkLevelList>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
title = sys.argv[4]
system_key = sys.argv[5]
description = sys.argv[6]
poc_name = sys.argv[7]
poc_phone = sys.argv[8]
poc_email = sys.argv[9]
add_user_to_system_package = sys.argv[10]
acronym = sys.argv[11]
framework_id = sys.argv[12]
framework_level_list = sys.argv[13]

data = {
    "title": title,
    "systemKey": system_key,
    "description": description,
    "pocName": poc_name,
    "pocPhone": poc_phone,
    "pocEmail": poc_email,
    "addUserToSystemPackage": add_user_to_system_package,
    "acronym": acronym,
    "frameworkId": framework_id,
    "frameworkLevelList": framework_level_list
}

endpoint = "/api/external/systempackage/"
url = f"{base_url}{endpoint}?applicationKey={app_key}"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"
headers["Content-Type"] = "application/x-www-form-urlencoded"

try:
    resp = requests.post(url, headers=headers, data=data)
    
    print(f"HTTP Status Code: {resp.status_code}")
    if resp.status_code == 200:
        print("System Package created successfully.")
    else:
        print("Error creating System Package:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")