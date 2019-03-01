#!/usr/bin/python
import xmltodict
from ncclient import manager
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass
from pprint import pprint

with open("xml_example.xml") as f:
   xml_example=f.read()

print(xml_example)
xml_dict = xmltodict.parse(xml_example)
int_name=xml_dict["configuration"]["interfaces"]["interface"]["name"]
print(int_name)
xml_dict["configuration"]["interfaces"]["interface"]["ipv4"]["address"]["ip"]="192.168.0.2"
print(xmltodict.unparse(xml_dict))

file=open("xml_output.xml",'w+')
file.write(xmltodict.unparse(xml_dict))
file.close()

juniper1 = {"host":"10.1.2.3", "user":'root', "password":'Juniper'}
a_device=Device(**juniper1)
a_device.open()

cfg=Config(a_device)


cfg.load(path="xml_output.xml", format="xml", merge=True)
print "Performing commit"
cfg.commit()

