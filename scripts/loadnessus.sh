# Load all Patch files from a particular folder
# curl -X POST -H "Accept: application/json" -H "Authorization: Bearer s.G72cdP24bwMsF3Oy2bdGdi1h" -F "patchscanFile=@./IDS-CONEX-HQ-closeditems.nessus"  http://192.168.13.114:8080/api/external/systempackage/degthatnetwork/patchscan/\?applicationKey\=degthatuploader

for i in $(find ../data/nessus-scans/*.nessus); do 
    eval curl -X POST -H \"Accept: application/json\" -H \"Authorization: Bearer s.Fl0KfrDNJwa2OHlt3RoFbF84\" -F \"checklistFile=\@$i\" http://192.168.13.114:8080/api/external/systempackage/degthatnetwork/patchscan/\?applicationKey\=degthatuploader -v;

    echo 'Uploaded "checklistFile=@'$i'"';

    sleep 1
done