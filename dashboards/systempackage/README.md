# System Package Dashboard
This is a system package dashboard, refreshing every 1 minute to load the changes on:
* number of checklists
* score for checklists
* score for patch vulnerabilities

You have to make the JSON API data source, point it to and then set up like the below screenshots.

## Grafana Dashboard
![Grafana Dashboard](./img/systempackage-dashboard.jpg?raw=true)

## OpenRMF<sup>&reg;</sup> Professional Dashboard
![Application Dashboard](./img/systempackage-listing.jpg?raw=true)

## JSON API Settings
use the `Authorization` and the value is `Bearer ` + your generated token

![Datasource Setting](./img/jsonapi-settings.png?raw=true)
