#!/usr/bin/python


from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass
from pprint import pprint

pwd=getpass()
ip_addr=raw_input("Enter Juniper IP: ")
ip_addr=ip_addr.strip()
juniper1 = {"host":ip_addr, "user":'root', "password":'Juniper'}
print "\n\nConnecting to Juniper...\n"
a_device=Device(**juniper1)
a_device.open()

cfg=Config(a_device)
print "Setting hostname using set notation"
cfg.load("set system host-name j9", format="set", merge=True)
print "Current config differences: "
print cfg.diff()
print "Performing rollback"
cfg.rollback(0)
print "\nSetting hostname usingXML (external file)"
cfg.load(path="load_hostname.xml", format="xml", merge=True)
print "Performing commit"
cfg.commit()
