#!/usr/bin/python2

import pyping

r=pyping.ping("192.168.122.11")
if r.ret_code == 0:
 print "Success"
else:
 print "failure"

