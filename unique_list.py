#!/usr/bin/python

size=int(raw_input("Enter the list size: "))
#  Initiate the list
list=[]

#  Append the data in list
for i in range(1,size+1):
	list.append(int(raw_input("Enter the "+str(i)+"th number: ")))

# Entered list is
print list

print "manipulated list is: "

list.sort()
t=0

for i in range(1,size):
	if list[t]==list[t+1]:
		list.remove(list[i-1])
	else:
		t+=1

print list

