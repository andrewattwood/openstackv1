#from confile import edit

#editint = edit()
#editint.afunction()

import ConfigParser
import os


#set variables for install
controllername  = "controller"



config = ConfigParser.RawConfigParser()
config.read('test.txt')

#print config.get('DEFAULT', 'verbose')
#config.set('DEFAULT', 'baz', 'fun') 
#config.remove_option('Section1', 'baz')
#config.add_section('Section1')

#os.system('')

os.system('apt-get install ubuntu-cloud-keyring')
os.system('echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu trusty-updates/kilo main" > /etc/apt/sources.list.d/cloudarchive-kilo.list')
os.system('apt-get update && apt-get -y upgrade')
os.system('apt-get install ntp')
os.system('rm /var/lib/ntp/ntp.conf.dhcp')

os.environ["DEBUSSY"] = "1"

#remove servers and add controller for ntp
os.system('grep -vh \'^[[:space:]]*server\' /etc/ntp.conf')
os.system(controllername + ' >> /etc/ntp.conf')


os.system('')
os.system('')
os.system('')
os.system('')
os.system('')


echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu trusty-updates/kilo main" > /etc/apt/sources.list.d/cloudarchive-kilo.list



with open('test.txt', 'wb') as configfile:
	config.write(configfile)

