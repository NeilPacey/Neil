#!/usr/bin/python
import xmltodict

with open("xml_example.xml") as f:
   xml_example=f.read()

print(xml_example)
xml_dict = xmltodict.parse(xml_example)
int_name=xml_dict["interface"]["name"]
print(int_name)
xml_dict["interface"]["ipv4"]["address"]["ip"]="192.168.0.2"
print(xmltodict.unparse(xml_dict))



from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass
from pprint import pprint

cfg.load(path="xml_changed.xml", format="xml", merge=True)
print "Performing commit"
cfg.commit()

