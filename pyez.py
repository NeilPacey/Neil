#!/usr/bin/python


from jnpr.junos import Device
from pprint import pprint
device1 = Device(host='10.1.2.3', user='root', password='Juniper')
device1.open()
pprint(device1.facts)
