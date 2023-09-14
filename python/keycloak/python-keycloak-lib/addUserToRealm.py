# Get a user record for the parameters passed in, if it is there
# fix formatting and return JSON
# to run:  python3 addUserToRealm.py https://keycloak.mycompany.com/auth/ admin 1wsx2wsx3edc4rfv openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH user.name user.email@soteriasoft.com firstname lastname mypassword

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
                        username=sys.argv[2],
                        password=sys.argv[3],
                        realm_name=sys.argv[4],
                        client_id=sys.argv[5],
                        client_secret_key=sys.argv[6],
                        verify=True)

keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

new_user = keycloak_admin.create_user({"email": sys.argv[8],
                                       "username": sys.argv[7],
                                       "enabled": True,
                                       "firstName": sys.argv[9],
                                       "lastName": sys.argv[10],                                       
                      "credentials": [{"value": sys.argv[11],"type": "password"}]},exist_ok=False)

if new_user is None:
    print("User not created successfully\n")
else:
    user_data = keycloak_admin.get_user(new_user)
    user_data = str(user_data).replace("'", '"')
    user_data = str(user_data).replace("True", 'true')
    user_data = str(user_data).replace("False", 'false')
    json_object = json.loads(user_data)
    print(json.dumps(json_object, indent=1))