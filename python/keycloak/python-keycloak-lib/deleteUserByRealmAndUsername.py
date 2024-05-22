# Delete the user for the realm and username parameters passed in, if it is there
# to run:  python3 deleteUserByRealmAndUsername.py https://keycloak.mycompany.com/auth/ openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH user.name

import sys
import json
from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenIDConnection

keycloak_connection = KeycloakOpenIDConnection(
                        server_url=sys.argv[1],
                        realm_name=sys.argv[2],
                        client_id=sys.argv[3],
                        client_secret_key=sys.argv[4],
                        verify=True)

keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

user_id_keycloak = keycloak_admin.get_user_id(sys.argv[5])
if user_id_keycloak is None:
    print("User Id was not found for that Username\n")
else:
    response = keycloak_admin.delete_user(user_id=user_id_keycloak)
    print(response)