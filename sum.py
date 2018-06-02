#!/usr/bin/python

# Sum will store on this
sum=0

print "enter the values to add and press '=' to execute "

while (1) :
	x=raw_input()
	if x == '=' :
		break
	else :
		sum=sum+int(x)

print 'SUM is : '+str(sum)

