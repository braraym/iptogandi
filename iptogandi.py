#!/usr/bin/env python

import configparser
import netifaces
import requests
import json

try:
	config = configparser.ConfigParser()
	config.read('/usr/local/etc/iptogandi.conf')

except Exception as e:
	print(e)
	exit(1)

errorCount = 0

for section in config.sections():
	try:
		apikey = config.get(section, 'apikey')
		interface = config.get(section, 'interface')
		domain = config.get(section, 'domain')
		record = {'type': config.get(section, 'record_type'), 'name': config.get(section, 'record_name'), 'ttl': config.getint(section, 'record_ttl')}

		print('Section: ' + section)
		ip = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']

		print('Updating the record to ' + ip)

		url = 'https://dns.api.gandi.net/api/v5/domains/' + domain + '/records/' + record['name'] + '/' + record['type']
		headers = {'Content-Type': 'application/json', 'X-Api-Key': apikey}
		data = {'rrset_ttl': record['ttl'], 'rrset_values': [ ip ]}

		response = requests.put(url, headers=headers, data=json.dumps(data))
		result = json.loads(response._content)
		print(result)

		if response.status_code != 201:
			errorCount += 1

	except Exception as e:
		print(e)
		exit(1)

exit(errorCount)
