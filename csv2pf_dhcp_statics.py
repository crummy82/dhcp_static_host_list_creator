import csv


# Set the variables below to match your dhcp subnet.
# If you have any other custom settings (eg. second DNS server, custom lease time, etc.)
# you will need to change/add those values below between each <> and </> tag.
# pfSense will not allow you to leave tags out of configs when importing so DO NOT
# delete unused configuration lines or you will get errors. 
# The interface name can be found in pfSense in Status->Interfaces in parentheses. The
# default is "lan" if you only have one internal LAN interface.

DHCP_RANGE_START = "192.168.1.10"
DHCP_RANGE_END = "192.168.1.250"
DNS_SERVER = "192.168.1.1"
INTERFACE_NAME = "lan"
LEASE_IN_LOCAL_TIME = "true"
DOMAIN = "lan.home"
UPDATE_DNS = "allow"


rows = [] # saves rows of data for each host

# Loops through CSV file and pulls each host's details. Hosts should be one per line in the file.
with open('host-list.csv') as hosts:
    for host in hosts:
        rows.append(host)

# Creates a new file 'static-dhcp-maps.xml' to export the config. It then uses the formatted 
# strings to loop through the rows list and populate the fields and write them to the file.
with open('static-dhcp-maps.xml', 'w') as statics:
    # First output the global dhcp configuration data to the file
    statics.write(f'''
<dhcpd>
	<{INTERFACE_NAME}>
		<enable></enable>
		<range>
			<from>{DHCP_RANGE_START}</from>
			<to>{DHCP_RANGE_END}</to>
		</range>
		<failover_peerip></failover_peerip>
		<dhcpleaseinlocaltime>{LEASE_IN_LOCAL_TIME}</dhcpleaseinlocaltime>
		<defaultleasetime></defaultleasetime>
		<maxleasetime></maxleasetime>
		<netmask></netmask>
		<gateway></gateway>
		<domain>{DOMAIN}</domain>
		<domainsearchlist></domainsearchlist>
		<ddnsdomain></ddnsdomain>
		<ddnsdomainprimary></ddnsdomainprimary>
		<ddnsdomainsecondary></ddnsdomainsecondary>
		<ddnsdomainkeyname></ddnsdomainkeyname>
		<ddnsdomainkeyalgorithm>hmac-md5</ddnsdomainkeyalgorithm>
		<ddnsdomainkey></ddnsdomainkey>
		<mac_allow></mac_allow>
		<mac_deny></mac_deny>
		<ddnsclientupdates>{UPDATE_DNS}</ddnsclientupdates>
		<tftp></tftp>
		<ldap></ldap>
		<nextserver></nextserver>
		<filename></filename>
		<filename32></filename32>
		<filename64></filename64>
		<filename32arm></filename32arm>
		<filename64arm></filename64arm>
		<rootpath></rootpath>
		<numberoptions></numberoptions>''')

    # Now loop through the list of static hosts to add those to the file
    for row in rows:
        host_details = row.split(',')
        statics.write(f'''
		<staticmap>
			<mac>{host_details[0]}</mac>
			<cid>{host_details[2]}</cid>
			<ipaddr>{host_details[1]}</ipaddr>
			<hostname>{host_details[2]}</hostname>
			<descr><![CDATA[{host_details[3]}]]></descr>
			<filename></filename>
			<rootpath></rootpath>
			<defaultleasetime></defaultleasetime>
			<maxleasetime></maxleasetime>
			<gateway></gateway>
			<domain></domain>
			<domainsearchlist></domainsearchlist>
			<ddnsdomain></ddnsdomain>
			<ddnsdomainprimary></ddnsdomainprimary>
			<ddnsdomainsecondary></ddnsdomainsecondary>
			<ddnsdomainkeyname></ddnsdomainkeyname>
			<ddnsdomainkeyalgorithm>hmac-md5</ddnsdomainkeyalgorithm>
			<ddnsdomainkey></ddnsdomainkey>
			<tftp></tftp>
			<ldap></ldap>
			<nextserver></nextserver>
			<filename32></filename32>
			<filename64></filename64>
			<filename32arm></filename32arm>
			<filename64arm></filename64arm>
			<numberoptions></numberoptions>
		</staticmap>''')

    # Finally ouput the global settings at the end of the config file and close
    statics.write(f'''		
		<dnsserver>{DNS_SERVER}</dnsserver>
		<dnsserver></dnsserver>
	</{INTERFACE_NAME}>
</dhcpd>''')
