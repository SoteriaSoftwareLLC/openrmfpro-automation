# Test that AuthN/AuthZ and Permissions are right
# curl -X POST -H "Content-Type: multipart/form-data" -H "Authorization: Bearer s.G72cdP24bwMsF3Oy2bdGdi1h" -F "applicationKey=degthatuploader"  http://192.168.13.74:8080/api/external/testauthentication -v

curl -X POST -H "Content-Type: multipart/form-data" -H "Authorization: Bearer s.Fl0KfrDNJwa2OHlt3RoFbF84" -F "applicationKey=degthatuploader"   http://192.168.13.114:8080/api/external/testauthentication -v