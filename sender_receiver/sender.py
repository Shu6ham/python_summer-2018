#!/usr/bin/python

import socket #Calling of  socket library

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


for i in range(1000):
	msg=raw_input("Enter your msg/reply :- \n")
	s.sendto(msg,("192.168.10.191",7777))	
	data=s.recvfrom(10000)
	print data[0]
	
	
