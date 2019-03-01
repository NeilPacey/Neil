#!/usr/bin/python
import telnetlib
import time
from ncclient import manager
user="root"
password="Juniper"
host="10.1.2.3"


with manager.connect(host=host, port=830, username=user, password=password, hostkey_verify=False, device_params={'name':'junos'}) as m:
    c=m.get_config(source='running').data_xml
    print
    with open("%s.xml" % host, 'w') as f:
        f.write(c)


