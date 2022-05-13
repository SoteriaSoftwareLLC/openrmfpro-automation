#!/bin/bash
# Test that AuthN/AuthZ and Permissions are right
curl -X POST -H "Authorization: Bearer hvs.xxxxxxxxxxxx" -F "applicationKey=openrmfprosvc" http://192.168.13.111:8080/api/external/testauthentication -v