# Automated Continuous Monitoring with Upload APIs

A very common scenario is using the APIs to automatically upload SCAP XCCDF .xml files and .nessus patch scan files from scheduled scans into OpenRMF<sup>&reg;</sup> Professional. This allows automating the continuous scanning and monitoring of machines in your system package to keep the vulnerability numbers up to date. 

You can do this from the start to add checklists to a new or empty system package. You can do this after you get everything in there loaded as well to keep them updated on a routine basis. Use the SCAP Upload APIs and Patch Upload APIs to accomplish this.

You could also combine with Scenario #1 above and use Organization Templates for those hostnames/devices to load the initial starter checklist into the system package. And then automate scans to update the automated checks that can be done. 

Using templates for DISA checklists or your own custom checklist templates, you can set the boilerplate manual checks to save time as well. Combine that with locked vulnerabilities and false positives can be less of a headache just the same. 