# OpenRMF<sup>&reg;</sup> Professional Sample Application
This is a sample application using NodeJS as the backend wrapping the OpenRMF<sup>&reg;</sup> Professional APIs in version 2.7. It shows selecting system packages, listing checklists, listing H/W, listing S/W and the like. It also has a template listing page.

This is done in HTML and JS with Bootstrap 5 only. There are a lot more ways to make a GUI and use OpenRMF<sup>&reg;</sup> Professional as a data source. This is just an example to get the development thoughts flowing. And this can be represented in dotnet core, Golang, Ruby, Java or any other language in a similar manner. This app just wraps the APIs, puts the ENV info for the token, application key and URL into the runtime, and lets it go.

## Environment Variables
This was done in VSCode. The .vscode has launch JSON information for the environment variables needed to wrap the API correctly. 
* "LISTENPORT" -- the port that your application listens on for the web interface, can be whatever you want it to be that works
* "ROOTAPIURL" -- the root URL to the external API based on DNS name, IP, etc. ending in /api/external
* "APIKEY" -- your API Key created for you, that tracks back to a user in OpenRMF with permissions and roles, especially the ExternalAPI role it needs
*  "APITOKEN" -- the token generated for that API key

## To Do
- [ ] add more to the demo application for uploading files, CKL, .Nessus, .XML SCAP results
- [ ] add a way to select templates and do the "bulk add checklists" injecting hostname to a system package

Feel free to Fork this repo, add your own ideas, and do a P/R for us to review and add into the community using this. The massive manual way we STILL do ATOs and FedRAMP/RMF approvals has passed its expiration date! And it is starting to stink. 

We need to do better!