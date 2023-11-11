# Example Code for Python 3.x to push and pull data from Keycloak for OpenRMF<sup>&reg;</sup> Professional
There is a manual folder for permforming all calls to authenticate, get a token, run commands. 

There is a separate Python-Keycloak folder to show automation using a publicly available library that encapsulates a lot of this and makes it easier. 

For the `python-keycloak` library to work you need to create a new OpenID Connect Client in whatever realm you wish to connect to (e.g. `openrmfpro`), and make sure the Capability Config has "client authentication" on, "direct access grants" checked and "service accounts roles" checked as well. Then make note of the Client Secret on the Credentials tab.

![Capability Config settings](./img/capability-config.png?raw=true)

Also, under the Service accounts roles tab, you can click Assign Role and add roles to ensure least privilege but execution of whatever functions you are working with to automate around Keycloak. Make sure you `Filter by clients` in the top corner of that Assign Role popup window to view the roles.  You can see where to start below.

![Capability Config settings](./img/service-accounts-roles.png?raw=true)

> Note that for OpenRMF Professional we use a `/auth/` path off Keycloak. That is not by default as of the version 20+ that we currently use in our application. However, we put Keycloak behind our NGINX proxy and had to include a path so we use the older `/auth/`. Make sure you have that in your connection configuration or you may receive a 404 "file not found" type of response on your python scripts.

## Install Requests Python Package

You will need to run `pip3 install requests` in order to load that library into your folder. Then you can start with the authentication.py script.

## Install prettytable Python Package

You will need to run `pip3 install prettytable` in order to load that library into your folder. Then you can start with the authentication.py script.

## Install the Python-Keycloak library

You will need to run `pip3 install python-keycloak` to add the proper library into your folder to call Keycloak with the scripts. See https://pypi.org/project/python-keycloak/ for more great information.  Those specific examples are under <a href="./python/keycloak/python-keycloak-lib/">python/keycloak/python-keycloak-lib/</a> specifically. 

## Calling the Python scripts

You could have a `.env` with the main parameters for the URL, realm admin user, etc. and pass in a password also. You would use `os.getenv('xxxxxxx')` and put the `.env` in the directory with the `.py` files to pull them in. For these examples you pass in every single thing. In production, that may get tiresome. 

```
import os
from dotenv import load_dotenv

load_dotenv()
```