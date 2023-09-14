# List all users in JSON by the realm you pass in
# to run:  python3 listUsersByRealm.py https://keycloak.mycompany.com/auth/ admin 1wsx2wsx3edc4rfv openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH

import sys
import json
from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenIDConnection

keycloak_connection = KeycloakOpenIDConnection(
                        server_url=sys.argv[1],
                        username=sys.argv[2],
                        password=sys.argv[3],
                        realm_name=sys.argv[4],
                        client_id=sys.argv[5],
                        client_secret_key=sys.argv[6],
                        verify=True)

print("debug: getting the admin connection set")
keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

print("debug: running through commands")
# User counter
count_users = keycloak_admin.users_count()
print("Number of Users: " + str(count_users))

# Get Users
users = keycloak_admin.get_users({})
users = str(users).replace("'", '"')
users = str(users).replace("True", 'true')
users = str(users).replace("False", 'false')
json_object = json.loads(users)
print(json.dumps(json_object, indent=1))