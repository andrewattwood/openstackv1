#from confile import edit

#editint = edit()
#editint.afunction()

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('test.txt')

print config.get('DEFAULT', 'verbose')

config.set('DEFAULT', 'baz', 'fun') 

#config.add_section('Section1')


with open('test.txt', 'wb') as configfile:
	config.write(configfile)

