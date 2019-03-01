#!/usr/bin/python2

import paramiko
import time

ip_address="192.168.122.11"
username="cisco"
password="cisco"
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)
print "Successful Connection", ip_address

remote_connection=ssh_client.invoke_shell()
remote_connection.send("configure terminal\n")

for n in range (2,21):
    print "creating VLAN " + str(n)
    remote_connection.send("vlan " + str(n) + "\n")
    remote_connection.send("name snt" + str(n) + "\n")
    time.sleep(0.5)

remote_connection.send("end\n")

time.sleep(1)
output=remote_connection.send("end\n")
print output

ssh_client.close
