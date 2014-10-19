#!/usr/bin/python

def power(m, n):
	p = 1;
	for i in range (1,n):
		p = p * m ;
		i = i + 1;
	return p;	
			

for  j in range(0,10):
	print "%d %d %d" % (j, power ( 2, j), power ( -3, j)) 

	
