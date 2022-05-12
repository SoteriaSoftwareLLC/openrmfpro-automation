#!/bin/bash
# Test that AuthN/AuthZ and Permissions are right
curl -X POST -H "Content-Type: multipart/form-data" -H "Authorization: Bearer s.xxxxxxxxxxxxxxxxxxxxxxx" -F "applicationKey=degthatuploader"   http://192.168.13.114:8080/api/external/testauthentication -v




curl -X POST -H "Accept: application/json" -H "Authorization: Bearer hvs.CAESIHOEmIExpnyN050DkvRpA6S5OeFh_TQ3OwfJNIINDYOsGh4KHGh2cy4xRXE5T1dvQU9XMnBRb2lwdFFkRVY1QjQ" -F "patchscanFile=./MachinaBio_System_Scan_Pre-Patch-Dec_2020.nessus" http://192.168.13.111:8080/api/external/systempackage/companyinfra/patchscan/?applicationKey=openrmfprosvc -v