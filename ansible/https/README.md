# Ansible Playbook setup and notes for automated HTTPS setup

* pass in the inventory with -i xxxxxxxxx
* pass in parameters with -e "sssssss=yyyyyyy" type of setup to override variables in the file
* you can use ansible facts to replace the IPV or HOSTNAME type of setup in the file as well.

```
sudo ansible-playbook convert-to-secure-port.yml
```

## Prerequisites

All the files in the variables file. 

Know 8443 versus 443.

Running currently at port 8080/ successfully first

## Variables to use

https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html#magic-variables

```
# ALL OF THESE ARE REQUIRED INCLUDING THE PEM FILE
# what is your DNS entry or IP address to access
# if using DNS, use all lowercase letters as Keycloak is case sensitive
target_dns_ip_entry: openrmfpro.mycompany.com
# variables for the HTTPS certificate setup playbook for OpenRMF Professional
# exact path to the root OpenRMF Professional files
target_openrmfpro_path: /apps/openrmfpro
# source path for the files below
source_cert_path: /home/openrmfproadmin/certificates
# files we need to setup and move for HTTPS
source_pem_file: dhparam.pem
source_crt_combined_file: server.crt
source_key_file: server.key
# port to use of 8443 or 443, used in "when" clauses
target_secure_port: 8443
# the Keycloak admin account setup used for setting the valid redirect URI
target_keycloak_admin: admin
target_keycloak_admin_password: 1qaz2WSX3edc4RFV
```

## Certbox for Let's Encrypt

https://faun.pub/enable-https-on-ec2-instance-without-elastic-load-balancer-f69cd57a8f3a 

Setup the CNAME / A record. 

Then stop OpenRMF Pro, run port 80 NGINX, get the cert, stop NGINX, startup OpenRMF Pro with the new certificate.

```
amazon-linux-extras enable nginx1

sudo yum install epel-release
sudo yum install certbot-nginx

sudo yum install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
```

Verify port 80 is open all the way through. Then stop NGINX as port 80 is used by the certbot.

```
sudo systemctl stop nginx
sudo systemctl disable nginx
```

Installs into the /usr/bin/certbot executable. Then run the below where `-d xxxx` passes in the domain names and alternatives you want to secure.

```
sudo certbot certonly --standalone -d demo.openrmfpro.com
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Requesting a certificate for demo.openrmfpro.com

Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/demo.openrmfpro.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/demo.openrmfpro.com/privkey.pem
This certificate expires on 2024-12-22.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.
```

Copy those PEM files to the proper place and update the ansible VARs for HTTPS properly

Make your dhparam file

Set it up and let it rip!