#!/usr/bin/python

import socket #Calling of  socket library

s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

s.bind(("127.0.0.1",9998))

for i in range(1000) :
	data=s.recvfrom(10000)
	print data[0]	
	msg=raw_input("Enter your reply :- \n")
	s.sendto(msg,data[1])
	

