# System Package Dashboard
This is a system package dashboard with more visuals for the open vulnerabilities, Cyber Readins numbers, and other data as well, refreshing every 1 minute to load the changes on:
* number of checklists
* score for checklists
* score for patch vulnerabilities
* score for other technology vulnerabilities

You have to make the JSON API data sources, point it to and then set up like the below screenshots.

> You can have a single data source that multiple dashboards use. Do not think it is a one-to-one dashboard to data source relationship

The JSON included here has named data sources.
* system package record vulnerabilities by categories
* cyber readiness numbers

You will have to install the JSON API data source, make them and point it to your system package, and then the rest of this works by copying/pasting the JSON into a new dashboard with the "Import" area under the Create "+" menu on the left of Grafana.

## Grafana Dashboard
![Grafana Dashboard](./img/dashboard-visuals.png?raw=true)

## OpenRMF<sup>&reg;</sup> Professional Dashboard
![Application Dashboard](./dashboard-ato-systempackagenumbers/systempackage-listing.png?raw=true)

## JSON API Settings
For the Custom HTTP Headers, use the `Authorization` and the value is `Bearer ` + your generated token. 

Note the Query string is your applicationKey=xxxxxxxxx without the `?` as it assumes that. 

Click Save and Test and make sure it is successful!

![Datasource Setting](./img/jsonapi-settings.png?raw=true)
