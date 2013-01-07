#!/usr/bin/env python
# This reducer reads output of Mapper which is in format
# HOUR 1
# it does aggregation and output hourly traffic
import sys
last_key = None
sum = 0

for line in sys.stdin:
        (key, val) = line.split("\t")
        if (last_key and last_key != key):
                print last_key + "\t" + str(sum)
                sum = 0
        sum += int(val)
        last_key = key
# for last key
print key + "\t" + str(sum)
