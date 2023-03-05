# ATO Vulnerability Status Dashboard with Notifications List
This is a dashboard showing all your ATO / system packages (the API user has access to as a Reader):
* title
* Checklist CAT 1, 2, 3 open vulnerabilities
* Patch vulnerabilities open by status of critical, high, medium, and low

You have to make the JSON API data source to point to the /systempackages/ endpoint, point it to and then set up like the below screenshots. There is a second one to point to the /notifications/ endpoint as well to show notifications. 

## Data Sources
The JSON included here has 2 named data sources, the notifications one is for the Notifications table. 
* system package listing `/systempackages/`
* notifications `/notifications/`

> You can have a single data source that multiple dashboards use. Do not think it is a one-to-one dashboard to data source relationship

You will have to install the JSON API data source, make them and point it to your system package, and then the rest of this works by copying/pasting the JSON into a new dashboard with the "Import" area under the Create "+" menu on the left of Grafana.

## Grafana Dashboard
![Grafana Dashboard](./img/vuln-status-listing-with-notifications.png?raw=true)

## OpenRMF<sup>&reg;</sup> Professional Dashboard
![Application Dashboard](../dashboard-ato-systempackagenumbers/img/systempackage-listing.png?raw=true)

## JSON API Settings
For the Custom HTTP Headers, use the `Authorization` and the value is `Bearer ` + your generated token. 

Note the Query string is your applicationKey=xxxxxxxxx without the `?` as it assumes that. 

Click Save and Test and make sure it is successful!

![Datasource Setting](../dashboard-ato-systempackagenumbers/img/jsonapi-settings.png?raw=true)