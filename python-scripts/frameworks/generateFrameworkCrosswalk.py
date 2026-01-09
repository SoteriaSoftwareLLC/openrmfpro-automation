# Generate a CSV we can use to upload a list of controls for a framework level/category based on another one
# API call from Developer's Guide: /api/external/controls/cciforcontrol/{frameworkId}/control/{controlDisplay/
# the framework ID you pass in is from the existing framework you want to map from
# you also pass in the new framework acronym, version, level category, and level value
# along with a CSV file that has two columns: existing control display and new control display
# The output is a CSV file named crosswalk-<new_framework_acronym>-<new_framework_version>.csv
# that can be used to upload the crosswalk mapping via the API

# ex: python3 generateFrameworkCrosswalk.py https://demo.openrmfpro.com openrmfprosvc hvs.xxxxxxxxxxxxxx 68cd32a0345e21f90a785792 CMMC "2.0" "Level 1" "" input-filename.csv

import sys
import json
import requests
import csv
import time
from requests.structures import CaseInsensitiveDict

# Check if we have enough arguments
if len(sys.argv) < 9:
    print("Usage: python3 generateFrameworkCrosswalk.py <url> <app_key> <token> <existing_framework_id> <new_framework_acronym> <new_framework_version> <new_framework_level> <new_framework_level_value> <input_filename.csv>")
    sys.exit(1)

def read_csv_to_array(filename):
    data_array = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) >= 2:  # Ensure there are at least two columns
                try:
                    # Convert to appropriate data types if needed (e.g., int, float)
                    column1_value = row[0]
                    column2_value = row[1]
                    data_array.append([column1_value, column2_value])
                except ValueError:
                    # Handle cases where conversion might fail
                    print(f"Skipping row due to data conversion error: {row}")
            else:
                print(f"Skipping row due to insufficient columns: {row}")
    return data_array

# call to make the input control array
my_control_array = read_csv_to_array(sys.argv[9])

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[3]

# make the name
csv_filename = 'crosswalk-' + sys.argv[5].replace(' ', '-') + '-' + sys.argv[6].replace(' ', '-') + '.csv'
# cycle through parameters and the data from the existing framework
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    # Write headers
    writer.writerow(['Framework Acronym', 'Framework Version', 'Framework Level Category', 'Framework Level Value', 'Control Display', 'CCIs'])
    cciList = ""

    for row in my_control_array:
        print(f"Processing control mapping: {row[0]} -> {row[1]}")
        url = sys.argv[1] + "/api/external/controls/cciforcontrol/" +sys.argv[4] + "/control/" + row[0] + "/?applicationKey=" + sys.argv[2]
        resp = requests.get(url, headers=headers)
        json_object = json.loads(resp.text)
        cciList = ""
        # print(resp.status_code)
        # print(json.dumps(json_object, indent=1))

        # Write the parameter values as a row
        for element in json_object:
            cciList += element['cciId'] + ", "
        # now write out the listing
        writer.writerow([sys.argv[5].strip(), sys.argv[6].strip(), sys.argv[7].strip(), sys.argv[8].strip(), row[1].strip(), cciList[:-2]])
        time.sleep(1)  # Pauses execution for 1 second

print(f"CSV file created: {csv_filename}")