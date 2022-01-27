from xml.dom import minidom

import csv

# User variables -
# DHCP_SUBNET is the dhcp subnet you want to create the static hosts for.
# IN_FILE is the config file from pfSense where the static host information will be pulled.
DHCP_SUBNET = '192.168.1.0/24'
IN_FILE = 'config-opnsense.xml'
OUT_FILE = 'static-dhcp-maps.xml'


# pfSense/OPNsense config file to parse
config_file = minidom.parse(IN_FILE)

# Starting line of config template to use
config_start = f'set service dhcp-server shared-network-name LAN subnet {DHCP_SUBNET} static-mapping '
# List of hosts to set as static assignments
hosts = []

# Grab the XML data for the statics tag
staticmap = config_file.getElementsByTagName('staticmap')

# Loop through all "staticmap" tag sections and pull the MAC, IP, and Hostname of each configured static host
for element in staticmap:
    mac = element.getElementsByTagName('mac')[0]
    ip = element.getElementsByTagName('ipaddr')[0]
    hostname = element.getElementsByTagName('hostname')[0]
    full_element = [hostname.firstChild.data, mac.firstChild.data, ip.firstChild.data]
    hosts.append(full_element)  # append each full host element to the list of hosts

# Open a file for writing and write out the config lines.
# These lines can then be copied and pasted into the command line configuration prompt on an Edgerouter.
try:
    with open(OUT_FILE, 'w') as statics:
        for host in hosts:
            statics.write(f'{config_start}{host[0]} mac-address {host[1]}\n')
            statics.write(f'{config_start}{host[0]} ip-address {host[2]}\n')
    print("Successfully created the config file!")

except:
    print("Creating the config file failed!")
