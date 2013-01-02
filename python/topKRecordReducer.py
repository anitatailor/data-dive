#!/usr/bin/env python
# Given value of K as argument 
# this script finds the keys with top K values 
# arg[1]: Column no
# arg[2]: Value of K

import sys
import heapq

topKQ = []
heapq.heapify(topKQ)

def insert_heap(key,val):
	tuple = (val, key)
	if (len(topKQ) < K):
		heapq.heappush(topKQ,tuple)
	else:
		heapq.heappushpop(topKQ,tuple)


def print_topK():
	print "size of priority q" + str(len(topKQ))
	for item in topKQ:
		(val,key) = heapq.heappop(topKQ)
		print key, "st \t", int(val)	
	(val,key) = heapq.heappop(topKQ)
	print key, "st \t", int(val)	

K = int(sys.argv[1])

(last_key, sum) = (None,0)

for line in sys.stdin:
	(key, val) = line.split("\t")
	if (last_key and last_key != key):
		# print last_key + "\t" + str(sum) 
		insert_heap(last_key,sum)
		sum = 0
	sum += int(val)
	last_key = key
# for last key
insert_heap(key,sum)
#print key + "\t" + str(sum)

print_topK()


