#!/usr/bin/python3
import getpass
import sys
import telnetlib
HOST="192.168.122.11"
user="cisco"
password="cisco"
tn=telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
tn.write(b"sh clock\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))

