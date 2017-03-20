#!/usr/bin/env python3

import configparser
import netifaces
import xmlrpc.client

try:
	config = configparser.ConfigParser()
	config.read('/etc/iptogandi.conf')

	api = xmlrpc.client.ServerProxy('https://rpc.gandi.net/xmlrpc/')

except Exception as e:
	print(e)
	exit(1)

for section in config.sections():
	try:
		apikey = config.get(section, 'apikey')
		interface = config.get(section, 'interface')
		domain = config.get(section, 'domain')
		record = {'type': config.get(section, 'record_type'), 'name': config.get(section, 'record_name')}
		record_ttl = config.getint(section, 'record_ttl')

		print('Section: ' + section)		
		
		zone_id = api.domain.info(apikey, domain)['zone_id']

		previous_ip = api.domain.zone.record.list(apikey, zone_id, 0, record)[0]['value']
		new_ip = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']

		print('Record\'s IP: ' + previous_ip)
		print('Current IP: ' + new_ip)

		if(previous_ip != new_ip):
			print('Updating the record...')
			new_zone_version = api.domain.zone.version.new(apikey, zone_id)
			new_record_id = api.domain.zone.record.list(apikey, zone_id, new_zone_version, record)[0]['id']
			new_record = {'name': record['name'], 'type': record['type'], 'value': new_ip, 'ttl': record_ttl}
			api.domain.zone.record.update(apikey, zone_id, new_zone_version, {'id':new_record_id}, new_record)
			print(api.domain.zone.version.set(apikey, zone_id, new_zone_version))

		print()

	except Exception as e:
		print(e)
		exit(1)

exit(0)
