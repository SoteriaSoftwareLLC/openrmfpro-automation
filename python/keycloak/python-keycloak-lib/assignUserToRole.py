# Get a user record for the parameters passed in, if it is there
# fix formatting and return JSON
# to run:  python3 assignUserToRole.py https://keycloak.mycompany.com/auth/ admin 1wsx2wsx3edc4rfv openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH user.name role.name

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

keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

user_id_keycloak = keycloak_admin.get_user_id(sys.argv[7])
role_keycloak = keycloak_admin.get_realm_role(sys.argv[8])

if user_id_keycloak is None:
    print("User Id was not found for that Username\n")
elif role_keycloak is None:
    print("Role was not found\n")
else:
    role_keycloak = str(role_keycloak).replace("'", '"')
    role_keycloak = str(role_keycloak).replace("True", 'true')
    role_keycloak = str(role_keycloak).replace("False", 'false')
    role_json_object = json.loads(role_keycloak)
    response = keycloak_admin.assign_realm_roles(user_id_keycloak, role_json_object)