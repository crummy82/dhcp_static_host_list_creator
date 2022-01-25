## DHCP Static Host List Creator ##
Scripts to create and convert DHCP static host assignments for **pfSense, OPNsense, Edgerouter,** and **VyOS** devices.

It is painstaking to add static dhcp hosts to firewalls/routers when you have lots of MAC addresses, IPs, and Hostnames to work with. These scripts can help. Currently there are two -
1. pfSense dhcp static host list creator - *csv2pf_dhcp_statics.py*
2. pfSense/OPNSense config file to Edgerouter/VyOS config script converter - *pf2vy_dhcp_statics.py*

#### pfSense Static Host List Creator ####
This is a script to create a pfSense config from a CSV file list in the following format on each line of the CSV file -
```
mac,IP,hostname,description
```
This will import the file 'host-list.csv' from the current directory and output the file 'static-dhcp-maps.xml' that can be imported into pfSense using the GUI Backup & Restore page.

#### pfSense/OPNSense to Edgerouter/VyOS dhcp static host converter ####
This script takes a config backup file from pfSense or OPNSense and converts it to a configuration script that can be copied and pasted into an Edgerouter or VyOS command line configuration prompt. The config backup file from pfSense or OPNSense can be a full config backup or just a config backup of the DHCP Server. 
Save the config backup file in the same directory as 'config.xml' and run the script. The script will output a file 'static-dhcp-maps.txt' file. The contents of this file can be pasted into the configuration prompt of your Edgerouter or VyOS device to configure all of your static dhcp hosts.
