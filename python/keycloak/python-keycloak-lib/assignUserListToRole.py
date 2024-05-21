# Assign a role to a list of users from the CSV passed in
# to run:  python3 assignUserListToRole.py https://keycloak.mycompany.com/auth/ openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH csvfilename rolename

import sys
import json
from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenIDConnection
import csv

keycloak_connection = KeycloakOpenIDConnection(
                        server_url=sys.argv[1],
                        realm_name=sys.argv[2],
                        client_id=sys.argv[3],
                        client_secret_key=sys.argv[4],
                        verify=True)

keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

csv_file = sys.argv[5]

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # skip the header row

    for row in csv_reader:
        user_id_keycloak = keycloak_admin.get_user_id(row[0].strip())
        role_keycloak = keycloak_admin.get_realm_role(sys.argv[6])

        if user_id_keycloak is None:
            print("User Id was not found for that Username " + row[0].strip() + "\n")
        elif role_keycloak is None:
            print("Role was not found for " + sys.argv[6] + "\n")
        else:
            role_keycloak = str(role_keycloak).replace("'", '"')
            role_keycloak = str(role_keycloak).replace("True", 'true')
            role_keycloak = str(role_keycloak).replace("False", 'false')
            role_json_object = json.loads(role_keycloak)
            response = keycloak_admin.assign_realm_roles(user_id_keycloak, role_json_object)
            print("Role " + sys.argv[6] + " assigned to User " + row[0].strip() + " successfully\n")