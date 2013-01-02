#!/usr/bin/env python
# Given column no and value of K as argument 
# this script finds the top K values of that column
# arg[1]: Column no to be analyzed

import sys
index = int(sys.argv[1])

for line in sys.stdin:
	fields = line.strip().split(",")
	if (fields[index].strip() != ""):
		print fields[index] + "\t" + "1"

	

