#!/usr/bin/python


from jnpr.junos import Device
from pprint import pprint
device1 = Device(host='10.1.2.3', user='root', password='Juniper')
device1.open()
pprint(device1.facts)

from jnpr.junos.op.ethport import EthPortTable
ports=EthPortTable(device1)
ports=get()

for k, v in ports['fe-0/0/1'].items():
 print k, v   
