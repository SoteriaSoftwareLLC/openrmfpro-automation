# Example Code for golang to push and pull data from OpenRMF<sup>&reg;</sup> Professional
The examples here assume you have OpenRMF® Professional v2.7 or higher installed, the external API setup and turned on, and you have at least one Application Integration record setup on the Administration --> External API Integration page. Your user account in Keycloak also must be setup to match the API integration with proper roles and permissions, including the ExternalAPI role to allow interaction from outside the OpenRMF<sup>&reg;</sup> Professional UI. 

Some of the APIs for patch vulnerabilities and the other technology vulnerabilities are version 2.8 or higher. If you have questions please see your customer representative or email Soteria Software Support. You can also contact us on our https://www.soteriasoft.com/ company website as well.

## Building the Examples
Perform a go build like below to build these simplified examples

```
go build -o listSystemPackages listSystemPackages.go 
```

## Running the Examples
Once built you can run the examples on your OS by calling the executable and passing in the required parameters. Most of the time you have to at least pass in the root URL, the application Key and the token for the open API setup for OpenRMF<sup>&reg;</sup> Professional at a minimum. Others you pass in the systemKey from your system package as well. And a few you pass in unique Ids of checklists or history items you are requesting.

```
./listSystemPackages http://192.168.13.25:8080 soteriaapi hvs.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```