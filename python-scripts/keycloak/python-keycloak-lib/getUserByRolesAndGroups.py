# Get a user record for the realm and username parameters passed in, if it is there
# fix formatting and return JSON
# to run:  python3 getUserByRolesAndGroups.py https://keycloak.mycompany.com/auth/ openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH user.name

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

# set the headers
userRolesGroupsTable = PrettyTable(["Roles", "Groups"], align='l', max_width=40)
userRolesGroupsTable.hrules=ALL

user_id_keycloak = keycloak_admin.get_user_id(sys.argv[5])
if user_id_keycloak is None:
    print("User Id was not found for that Username\n")
else:
    user_data = keycloak_admin.get_user(user_id_keycloak)
    user_data = str(user_data).replace("'", '"')
    user_data = str(user_data).replace("True", 'true')
    user_data = str(user_data).replace("False", 'false')
    user_json_object = json.loads(user_data)
    #print(json.dumps(user_json_object, indent=1))
    
    usernameRoles = []
    usernameGroups = []

    # to get a list of user roles
    userRoles = keycloak_admin.get_all_roles_of_user(user_id= ["id"])
    userRoles = str(userRoles).replace("'", '"')
    userRoles = str(userRoles).replace("True", 'true')
    userRoles = str(userRoles).replace("False", 'false')
    userRoles_json_object = json.loads(userRoles)

    # for each role in the embedded listing, put into an array
    for roleName in userRoles_json_object["realmMappings"]:
        if (roleName["name"] not in "default-roles-openrmfpro"):
            usernameRoles.append(roleName["name"])

    # get all the groups
    userGroups = keycloak_admin.get_user_groups(user_id=["id"])
    userGroups = str(userGroups).replace("'", '"')
    userGroups = str(userGroups).replace("True", 'true')
    userGroups = str(userGroups).replace("False", 'false')
    userGroups_json_object = json.loads(userGroups)
    # get all the group names and put into an array
    for groupName in userGroups_json_object:
        usernameGroups.append(groupName["name"])

    userRolesGroupsTable.add_row([user_json_object["id"],user_json_object["username"],user_json_object["firstName"],user_json_object["lastName"],user_json_object["email"]])
# print the table out
print(userRolesGroupsTable)