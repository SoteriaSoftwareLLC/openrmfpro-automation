# OpenRMF<sup>&reg;</sup> Professional API Automation
This repo contains OpenRMF<sup>&reg;</sup> Professional API automation scripts and code to POST, PUT, and GET information via the External API. The External API was introduced as a main feature in v2.6 and vastly improved in v2.7 released in January 2022. Later versions will expand on this as well, as will the examples in this repo.

This repo goes along with the <a href="https://www.soteriasoft.com/" target="_blank">OpenRMF<sup>&reg;</sup> Professional</a> application and the Developer's Guide from Soteria Software to automate ingest and download of data to/from OpenRMF Professional. Please contact <a href="https://www.soteriasoft.com/contact.html#contactform">Soteria Software</a> for more information.

## How this Repo is Organized

The <a href="./scenarios">scenarios</a> folder explains a few scenarios around the APIs to get your creative juices flowing through your brain and getting your team communicating around ideas. 

The <a href="./data">data</a> for checklists, SCAP scans and Nessus/ACAS scans is in the data directory. Your scripts can pull from that sample data as examples. 

Each type of technology / language is organized in its own folder for dotnet core, golang, python, and scripts to just show examples. Your folder structure, URL, key, token, systemKey for data will be different but similar. 

The <a href="./dashboards">dashboards</a> folder show mainly Grafana dashboards pulling data from the OpenRMF<sup>&reg;</sup> Professional API as well using the JSON API datasource for Grafana.

The <a href="./applications">applications</a> folder has an example NodeJS application in it. This was done in VSCode. The .vscode has launch JSON information for the environment variables needed to wrap the API correctly. 
* "LISTENPORT" -- the port that your application listens on for the web interface, can be whatever you want it to be that works
* "ROOTAPIURL" -- the root URL to the external API based on DNS name, IP, etc. ending in /api/external
* "APIKEY" -- your API Key created for you, that tracks back to a user in OpenRMF with permissions and roles, especially the ExternalAPI role it needs
*  "APITOKEN" -- the token generated for that API key

## To Do
- [ ] add more to the demo application for uploading files, CKL, .Nessus, .XML SCAP results
- [ ] show how to select templates and do the "bulk add checklists" injecting hostname to a system package
- [ ] dotnet core 6.x examples calling APIs
- [ ] golang examples calling APIs
- [ ] java examples calling APIs
- [ ] more scenarios to list

# Note to Developers
Feel free to Fork this repo, add your own ideas, and do a P/R for us to review and add into the community using this. 

The massive manual way we STILL do ATOs and FedRAMP/RMF approvals has passed its expiration date! And it is starting to stink. 

We need to do better!