import csv


rows = []

with open('host-list.csv') as hosts:
	for host in hosts:
		rows.append(host)

with open('static-dhcp-maps.xml', 'w') as statics:
	for row in rows:
		statics.write(f'''
			<staticmap>
			<mac>{row[0]}</mac>
			<cid>{row[2]}</cid>
			<ipaddr>{row[1]}</ipaddr>
			<hostname>{row[2]}</hostname>
			<descr><![CDATA[{row[3]}]]></descr>
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
		</staticmap>
		''')


