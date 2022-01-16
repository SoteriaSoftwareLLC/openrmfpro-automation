# Load all SCAP Scan XCCDF XML files from a particular folder
for i in $(find ../data/scap-scans/*.xml); do 
    eval curl -X POST -H \"Accept: application/json\" -H \"Authorization: Bearer s.xxxxxxxxxxxxxxxxxxxxxxx\" -F \"checklistFile=\@$i\" http://192.168.13.114:8080/api/external/systempackage/degthatnetwork/scapchecklist/\?applicationKey\=degthatuploader -v;

    echo 'Uploaded "checklistFile=@'$i'"';

    sleep 1
done