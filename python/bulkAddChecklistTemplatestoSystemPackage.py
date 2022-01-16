import requests
from requests.structures import CaseInsensitiveDict

# Assign the API variables that are needed within the request's URL

APIname = 'systempackage' # Constant for this particular API
AppKey = 'applicationKey=aspirenineuploader'  # "aspirenineuploader is an example application key - replace it.
SystemKey = "aspireninetest"
TemplateIds="61b9e3df407f722ecf0ca361,61b9e3d4407f722ecf0ca2b6,61b9e3dd407f722ecf0ca345" 

checklistHostname="FILESVR1"

# Assign the request headers for this particular API
headers = CaseInsensitiveDict() # Does not change
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Authorization"] = "Bearer s.xxxxxxxxxxxxxxxxxxxxxxx"

# Build the API URL in order to make the request

url = ("http://192.168.13.114:8080/api/external/"+APIname+"/"+SystemKey+"/bulkadd/?"+ AppKey)
data = "templateIds="+TemplateIds+"&checklistHostname="+checklistHostname

# Make the API request
resp = requests.post(url, headers=headers, data=data)

# print to the screen the status code (i.e. 200, 400, 404, etc)
print(resp.status_code)

#print(resp.json)
print(resp.text)
