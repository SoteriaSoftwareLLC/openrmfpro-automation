# List all users and their roles in JSON by the realm you pass in
# to run:  python3 listUsersByRealmWithRoles.py https://keycloak.mycompany.com/auth/ openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH

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

keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

# Get Users
users = keycloak_admin.get_users({})
users = str(users).replace("'", '"')
users = str(users).replace("True", 'true')
users = str(users).replace("False", 'false')
# load the JSON
user_json_object = json.loads(users)
# set the headers
userRolesGroupsTable = PrettyTable(["Username", "Email", "Roles", "Groups"], align='l', max_width=60)
userRolesGroupsTable.hrules=ALL

# for each user JSON record
for item in user_json_object:
    # grab the user id in the "id" field
    username = item["username"]
    useremail = item["email"]
    usernameRoles = []
    usernameGroups = []

    # to get a list of user roles
    userRoles = keycloak_admin.get_all_roles_of_user(item["id"])
    userRoles = str(userRoles).replace("'", '"')
    userRoles = str(userRoles).replace("True", 'true')
    userRoles = str(userRoles).replace("False", 'false')
    userRoles_json_object = json.loads(userRoles)

    # for each role in the embedded listing, put into an array
    for roleName in userRoles_json_object["realmMappings"]:
        if (roleName["name"] not in "default-roles-openrmfpro"):
            usernameRoles.append(roleName["name"])

    # get all the groups
    userGroups = keycloak_admin.get_user_groups(item["id"])
    userGroups = str(userGroups).replace("'", '"')
    userGroups = str(userGroups).replace("True", 'true')
    userGroups = str(userGroups).replace("False", 'false')
    userGroups_json_object = json.loads(userGroups)
    # get all the group names and put into an array
    for groupName in userGroups_json_object:
        usernameGroups.append(groupName["name"])

    userRolesGroupsTable.add_row([username, useremail, ', '.join(map(str, usernameRoles)), ', '.join(map(str, usernameGroups))])
# print the table out
print(userRolesGroupsTable)