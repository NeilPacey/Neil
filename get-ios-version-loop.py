#!/usr/bin/python3
import telnetlib
import time
user="cisco"
password="cisco"
addresses=["192.168.122.11","192.168.122.12","192.168.122.13"]
for ip in addresses:
    tn=telnetlib.Telnet(ip)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    tn.write(b"sh version\n")
    tn.write(b"end\n")
    time.sleep(3)
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
    tn.close()
print(b"\n\n\n" + b"Complete")
