from xml.dom import minidom

import csv


# pfSense/OPNsense config file to parse
config_file = minidom.parse('config-opnsense.xml')
# Target subnet in Edgerouter/VyOS static DHCP scope
subnet = '192.168.1.0/24'
# Starting line of config template to use
config_start = f'set service dhcp-server shared-network-name LAN subnet {subnet} static-mapping '
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

# Open a config file script for writing and write out the config lines to use on Edgerouter/VyOS host
try:
    with open('static-dhcp-maps.txt', 'w') as statics:
        for host in hosts:
            statics.write(f'{config_start}{host[0]} mac-address {host[1]}\n')
            statics.write(f'{config_start}{host[0]} ip-address {host[2]}\n')
    print("Successfully created the config file!")

except:
    print("Creating the config file failed!")
