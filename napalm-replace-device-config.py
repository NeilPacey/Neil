
from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('192.168.122.11','cisco','cisco')
device.open()
device.load_replace_candidate(filename='./ios/new.cfg')
print device.compare_config()

###### when ready 

device.commit_config()

###### or, if not

device.discard_config()

###### merging config

device.load_merge_candidate(config= 'hostname newName\ninterface Ethernet\ndescription someText')
print device.compare_config()

######### rollback

device.rollback()

#### at the end of the session

device.close()
