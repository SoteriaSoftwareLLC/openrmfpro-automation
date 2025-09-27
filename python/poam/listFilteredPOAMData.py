# list the filtered POAM data
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/poams/?applicationKey={applicationKey}
# ex: python3 listFilteredPOAMData.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx degthatnetwork

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 29:
    print(
        "Usage: python3 listFilteredPOAMData.py "
        "<URL> <applicationKey> <token> <systemKey> "
        "<days> <relevance> <likelihood> <impact> <residualrisk> "
        "<resultingrisk> <severity> <status> <rawseverity> <showManual> "
        "<showChecklist> <showPatch> <showCompliance> <showInherited> "
        "<showTechVuln> <milestoneEventId> <grouped> <onlyMitigations> "
        "<begin> <end> <completedByDate> <needsUpdated> <securityCheck> "
        "<onlyFalsePositives> <onlyMisleadingInformation>"
    )
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]
system_key = sys.argv[4]
days = sys.argv[5]
relevance = sys.argv[6]
likelihood = sys.argv[7]
impact = sys.argv[8]
residualrisk = sys.argv[9]
resultingrisk = sys.argv[10]
severity = sys.argv[11]
status = sys.argv[12]
rawseverity = sys.argv[13]
show_manual = sys.argv[14]
show_checklist = sys.argv[15]
show_patch = sys.argv[16]
show_compliance = sys.argv[17]
show_inherited = sys.argv[18]
show_tech_vuln = sys.argv[19]
milestone_event_id = sys.argv[20]
grouped = sys.argv[21]
only_mitigations = sys.argv[22]
begin = sys.argv[23]
end_date = sys.argv[24]
completed_by_date = sys.argv[25]
needs_updated = sys.argv[26]
security_check = sys.argv[27]
only_false_positives = sys.argv[28]
only_misleading_information = sys.argv[29]

endpoint = "/api/external/systempackage/{systemKey}/poams/"
url = f"{base_url}{endpoint.replace('{systemKey}', system_key)}"

# Parameters for filtering (a very restrictive example derived from the doc's example for demonstration)
params = {
    "applicationKey": app_key,
    "days": days,
    "relevance": relevance,
    "likelihood": likelihood,
    "impact": impact,
    "residualrisk": residualrisk,
    "resultingrisk": resultingrisk,
    "severity": severity,
    "status": status,
    "rawseverity": rawseverity,
    "showManual": show_manual,
    "showChecklist": show_checklist,
    "showPatch": show_patch,
    "showCompliance": show_compliance,
    "showInherited": show_inherited,
    "showTechVuln": show_tech_vuln,
    "milestoneEventId": milestone_event_id,
    "grouped": grouped,
    "onlyMitigations": only_mitigations,
    "begin": begin,
    "end": end_date,
    "completedByDate": completed_by_date,
    "needsUpdated": needs_updated,
    "securityCheck": security_check,
    "onlyFalsePositives": only_false_positives,
    "onlyMisleadingInformation": only_misleading_information
}

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.get(url, headers=headers, params=params)
    
    print(f"HTTP Status Code: {resp.status_code}")

    if resp.status_code == 200:
        json_object = resp.json()
        print(json.dumps(json_object, indent=1))
    else:
        print("Error retrieving Filtered POAM Data:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")