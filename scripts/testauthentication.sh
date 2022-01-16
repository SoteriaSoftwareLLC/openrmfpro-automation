#!/bin/bash
# Test that AuthN/AuthZ and Permissions are right
curl -X POST -H "Content-Type: multipart/form-data" -H "Authorization: Bearer s.xxxxxxxxxxxxxxxxxxxxxxx" -F "applicationKey=degthatuploader"   http://192.168.13.114:8080/api/external/testauthentication -v