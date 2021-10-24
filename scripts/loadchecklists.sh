#!/bin/bash

# Load all Checklist CKL files from a particular folder
# curl -X POST -H "Accept: application/json" -H "Authorization: Bearer s.G72cdP24bwMsF3Oy2bdGdi1h" -F "checklistFile=@./DEGTHAT_SCC-5.0.1_2019-04-19_170849_XCCDF-Results_Microsoft_Word_2016-001.001.xml"  http://192.168.13.74:8080/api/external/systempackage/degthatnetwork/scapchecklist/\?applicationKey\=degthatuploader

for i in $(find ../data/checklists/*.ckl); do 
    eval curl -X POST -H \"Accept: application/json\" -H \"Authorization: Bearer s.Fl0KfrDNJwa2OHlt3RoFbF84\" -F \"checklistFile=\@$i\" http://192.168.13.114:8080/api/external/systempackage/degthatnetwork/scapchecklist/\?applicationKey\=degthatuploader -v;

    echo 'Uploaded "checklistFile=@'$i'"';

    sleep 1
done