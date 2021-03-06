# Example Code for Python 3.x to push and pull data from OpenRMF<sup>&reg;</sup> Professional
The examples here assume you have OpenRMF<sup>&reg;</sup> Professional v2.7 or higher installed, the external API setup and turned on, and you have at least one Application Integration record setup on the Administration --> External API Integration page. Your user account in Keycloak also must be setup to match the API integration with proper roles and permissions, including the ExternalAPI role to allow interaction from outside the OpenRMF<sup>&reg;</sup> Professional UI.

Some of the APIs for patch vulnerabilities and the other technology vulnerabilities are version 2.8 or higher. If you have questions please see your customer representative or email Soteria Software Support. You can also contact us on our https://www.soteriasoft.com/ company website as well.

## Install Requests

You will need to run `pip3 install requests` in order to load that library into your folder. Then you can start with the authentication.py script.

## Testing Authentication

To ensure your authentication is valid using the simple script for testauthentication.sh in the <a href="../scripts/">scripts</a> folder and make sure it prints back 200 as the request status. If so then your API call, structure, API Key, Token and user/pwd combination for that API are all valid.

## API Calls

The API calls here follow the OpenRMF<sup>&reg;</sup> Professional Developer's Guide. Please contact <a href="https://www.soteriasoft.com/resources/contact.html">Soteria Software</a> for more information.

## Notes
* for the Download XLSX scripts, there needs to be a ./download/ directory created where you run it. Or modify as appropriate.