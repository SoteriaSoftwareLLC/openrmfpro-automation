# assign a user to a group passed in
# to run:  python3 assignUserToGroup.py https://keycloak.mycompany.com/auth/ openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH user.name group.name

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
group_keycloak = keycloak_admin.get_group_by_path(path='/'+sys.argv[6])

if user_id_keycloak is None:
    print("User Id was not found for that Username\n")
elif group_keycloak is None:
    print("Group Id was not found for that Group name\n")
else:
    group_keycloak = str(group_keycloak).replace("'", '"')
    group_keycloak = str(group_keycloak).replace("True", 'true')
    group_keycloak = str(group_keycloak).replace("False", 'false')
    group_json_object = json.loads(group_keycloak)
    response = keycloak_admin.group_user_add(user_id_keycloak, group_json_object['id'])
    print("Group assigned to User successfully\n")