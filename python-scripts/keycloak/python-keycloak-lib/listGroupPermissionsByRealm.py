# List all group permissions in JSON by the realm you pass in
# to run:  python3 listGroupPermissionsByRealm.py https://keycloak.mycompany.com/auth/ openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH

import sys
import json
from prettytable import PrettyTable, ALL
from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenIDConnection

keycloak_connection = KeycloakOpenIDConnection(
                        server_url=sys.argv[1],
                        realm_name=sys.argv[2],
                        client_id=sys.argv[3],
                        client_secret_key=sys.argv[4],
                        verify=True)

print("debug: getting the admin connection set")
keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

# set the headers
realmTable = PrettyTable(["ID", "Name", "Path"], align='l', max_width=40)
realmTable.hrules=ALL

realm_groups = keycloak_admin.get_groups()

# Get Realms
realm_groups = str(realm_groups).replace("'", '"')
realm_groups = str(realm_groups).replace("True", 'true')
realm_groups = str(realm_groups).replace("False", 'false')
realm_json_object = json.loads(realm_groups)
#print(json.dumps(realm_json_object, indent=1))

for item in realm_json_object:
    realmTable.add_row([item["id"],item["name"],item["path"]])
# print the table out
print(realmTable)