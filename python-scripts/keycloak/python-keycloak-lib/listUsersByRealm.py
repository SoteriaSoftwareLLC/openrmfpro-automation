# List all users in JSON by the realm you pass in
# to run:  python3 listUsersByRealm.py https://keycloak.mycompany.com/auth/ openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH

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
userTable = PrettyTable(["ID", "Username", "First Name", "Last Name", "Email"], align='l', max_width=40)
userTable.hrules=ALL

print("debug: running through commands")
# User counter
count_users = keycloak_admin.users_count()
print("Number of Users: " + str(count_users))

# Get Users
users = keycloak_admin.get_users({})
users = str(users).replace("'", '"')
users = str(users).replace("True", 'true')
users = str(users).replace("False", 'false')
user_json_object = json.loads(users)
#print(json.dumps(json_object, indent=1))

for item in user_json_object:
    userTable.add_row([item["id"],item["username"],item["firstName"], item["lastName"],item["email"]])
# print the table out
print(userTable)