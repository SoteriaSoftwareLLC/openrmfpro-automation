# OpenRMF<sup>&reg;</sup> Professional API Automation
This repo contains OpenRMF<sup>&reg;</sup> Professional API automation scripts and code to POST, PUT, and GET information via our open API. The API was introduced as a main feature in v2.6 late summer 2021 and vastly improved in v2.7 released in January 2022 and again in v2.8. and beyond. Later versions will expand on this even further, as will the examples in this repo. Subscribe to the repo to get notifications on updates.

> The data, example applications, python scripts, and more are free to use as-is. Soteria Software supports the OpenRMF Professional application itself. However, the data here and python examples show how to use that application. The scripts and data here are representative data. If you wish to use them, please do. You may need to update them, put error checking, data formatting, and more as additional steps if you use these in production. 

This repo goes along with the <a href="https://www.soteriasoft.com/" target="_blank">OpenRMF<sup>&reg;</sup> Professional</a> application and the Developer's Guide from Soteria Software to automate ingest and download of data to/from OpenRMF Professional. Please contact <a href="https://www.soteriasoft.com/contact.html#contactform">Soteria Software</a> for more information.

## How this Repo is Organized

### Scenarios
The <a href="./scenarios">scenarios</a> folder explains a few scenarios around the APIs to get your creative juices flowing through your brain and getting your team communicating around ideas. 

### Data
The <a href="./data">data</a> for checklists, SCAP scans and Nessus/ACAS scans, and Audit Compliance scans based on DISA or CIS benchmarks is in the data directory. Your scripts can pull from that sample data as examples.  There are also example custom checklists created with our Custom Checklist wizard for all the manual policy, process, and procedure requirements in cyber compliance (i.e. NIST Control families like PM, AT, IR, PL, SA, RA).

* Nessus Patch Vulnerability Scans
* DISA CKLs
* Evaluate-STIG checklists
* Tanium CSV SCAP results
* Nessus SCAP
* other SCAP results
* Nessus audit compliance scans for 
* Software / Container vulnerability data
* Universal format Patch vulnerability data
* Lists for hardware, software, ports/protocols/services
* Lists for mitigation statements
* Lists for compliance statements
* Rapid7 Nexpose scan data
* Reading data from dashboards, scores, and compliance

Each type of technology / language is organized in its own folder for dotnet core, golang, python, and scripts to just show examples. Your folder structure, URL, key, token, systemKey for data may be different but similar. 

### Sample Dashboards
The <a href="./dashboards">dashboards</a> folder show mainly Grafana dashboards pulling data from the OpenRMF<sup>&reg;</sup> Professional API as well using the JSON API datasource for Grafana.

### Sample Applications
The <a href="./applications">applications</a> folder has an (older) example NodeJS application in it. This was done in VSCode. The .vscode has launch JSON information for the environment variables needed to wrap the API correctly. 
* "LISTENPORT" -- the port that your application listens on for the web interface, can be whatever you want it to be that works
* "ROOTAPIURL" -- the root URL to the external API based on DNS name, IP, etc. ending in /api/external
* "APIKEY" -- your API Key created for you, that tracks back to a user in OpenRMF with permissions and roles, especially the ExternalAPI role it needs
*  "APITOKEN" -- the token generated for that API key

### Scripts showing API calls

The <a href="./python">python</a> folder has python 3 scripts organized to show almost all of the API calls as well as a few combination calls.

The <a href="./dotnet-core">dotnet-core</a> folder has example .NET Core API call examples. 

The <a href="./golang">golant</a> folder has example Go language API call examples. 

The <a href="./scripts">scripts</a> folder has bash shell scripts with `curl` to call APIs with examples as well. 

## Swagger.json

The swagger.json file in the root of this repo shows calls as of OpenRMF<sup>&reg;</sup> Professional v2.10 API. Check the Developers Guide for this version to understand the calls and data formats.

# Note to Developers
Feel free to Fork this repo, add your own ideas, and do a P/R for us to review and add into the community using this. 

The massive manual way we STILL do ATOs and FedRAMP/RMF approvals has passed its expiration date! And it is starting to stink. 

We need to do better!

See more information at https://www.soteriasoft.com/ as well as our links on that site to our YouTube videos and scenarios.