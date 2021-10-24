# Example Code for bash scripts to push and pull data from OpenRMF<sup>&reg;</sup> Professional
The examples here assume you have at least OpenRMF<sup>&reg;</sup> Professional v2.6 installed, the external API setup and turned on, and you have at least one Application Integration record setup on the Administration --> External API Integration page. Your user account in Keycloak also must be setup to match the API integration with proper roles and permissions, including the ExternalAPI role to allow interaction from outside the OpenRMF<sup>&reg;</sup> Professional UI.


## Running the Test Authentication Example
When you run the testauthentication.sh type of script you should get a message similar to below. You need to update the script to make sure you update the following to your environment:
* Application Key from the External API Integration Generate Token function
* Authorization Bearer Token from the External API Integration Generate Token function
* HTTP/S URL to the root of your OpenRMF<sup>&reg;</sup> Professional installation


You should get a result similar to below showing 200 OK. Once this is setup correctly you should be able to get all the rest of the scripts here running correctly. You should check the above 3 items if any of the uploads or downloads do not work.
```
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 192.168.13.114...
* TCP_NODELAY set
* Connected to 192.168.13.114 (192.168.13.114) port 8080 (#0)
> POST /api/external/testauthentication HTTP/1.1
> Host: 192.168.13.114:8080
> User-Agent: curl/7.64.1
> Accept: */*
> Authorization: Bearer s.Fl0KfrDNJwa2OHlt3RoFbF84
> Content-Length: 164
> Content-Type: multipart/form-data; boundary=------------------------09d35726766f3e67
> 
* We are completely uploaded and fine
< HTTP/1.1 200 OK
< Server: nginx
< Date: Sun, 24 Oct 2021 12:26:38 GMT
< Content-Length: 0
< Connection: keep-alive
< X-Frame-Options: deny
< X-Content-Type-Options: nosniff
< X-XSS-Protection: 1; mode=block
< 
* Connection #0 to host 192.168.13.114 left intact
* Closing connection 0

```