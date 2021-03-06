#!/bin/bash
# Load all Patch files from a particular folder
# Realize it just lists the files, not in any particular order
# For loading older data you will want to sort the results by date or something

for i in $(find ../data/nessus-scans/*.nessus); do 
    eval curl -X POST -H \"Accept: application/json\" -H \"Authorization: Bearer s.xxxxxxxxxxxxxxxxxxxxxxx\" -F \"patchscanFile=\@$i\" http://192.168.13.114:8080/api/external/systempackage/degthatnetwork/patchscan/\?applicationKey\=degthatuploader -v;

    echo 'Uploaded "patchscanFile=@'$i'"';

    sleep 1
done