# Dashboards

This is an area to expand OpenRMF<sup>&reg;</sup> Professional as far as pulling data from APIs and displaying on dashboards.

Most of the Dashboards here are Grafana and use the JSON API data source for Grafana at https://grafana.com/grafana/plugins/marcusolsson-json-datasource/. You can add that plugin, reset Grafana, and then use that data source to point to an OpenRMF<sup>&reg;</sup> Professional API.

## Install the JSON API Plugin
As the `admin` user for Grafana, click the Server Admin icon and then Plugins. 

![List the Plugins](./img/install-plugins.png?raw=true)

Then click the JSON API plugin and click Install. 

![Install the Plugin](./img/jsonapi-plugin.png?raw=true)

Now that it is installed and ready for you go to the Datasource page.

![List Datasources](./img/install-plugins.png?raw=true)

Add the Datasource using the new JSON API Plugin.

![Use the JSON API Plugin](./img/addjsondatasource.png?raw=true)

## References

* https://grafana.com/grafana/plugins/marcusolsson-json-datasource/