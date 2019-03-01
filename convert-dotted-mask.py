#!/usr/bin/python3
address="192.168.122.11"
dotted_mask="255.255.255.0"
count=0
octets=0
for x in dotted_mask.split():
  count=count+1
  if count==1:
        first_octet=x
  elif x==2:
        second_octet=x 
  elif x==3:
        third_octet=x
  elif x==4:
        fourth_octet=x  

if int(first_octet)=255:
  bits=8
else:
  bits
