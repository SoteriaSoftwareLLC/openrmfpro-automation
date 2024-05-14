# Get a user record for the parameters passed in, if it is there
# fix formatting and return JSON
# to run:  python3 addUserToRealm.py https://keycloak.mycompany.com/auth/ admin 1qaz2WSX3edc4RFV openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH user.name user.email@soteriasoft.com firstname lastname mypassword

#############################################################################
# Please make sure if you use special characters you only use &, *, ( or ) 
# for your password as some of the other characters are reserved.
#############################################################################

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

new_user = keycloak_admin.create_user({"email": sys.argv[6],
                                       "username": sys.argv[5],
                                       "enabled": True,
                                       "firstName": sys.argv[7],
                                       "lastName": sys.argv[8],                                       
                      "credentials": [{"value": sys.argv[9],"type": "password"}]},exist_ok=False)

if new_user is None:
    print("User was not created successfully\n")
else:
    user_data = keycloak_admin.get_user(new_user)
    user_data = str(user_data).replace("'", '"')
    user_data = str(user_data).replace("True", 'true')
    user_data = str(user_data).replace("False", 'false')
    json_object = json.loads(user_data)
    print(json.dumps(json_object, indent=1))
    print("User was created successfully\n")