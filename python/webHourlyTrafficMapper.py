#!/usr/bin/env python
# This script reads apache web setver access.log and 
# Map each record to hours
# it's output is HOUR 1
# Reducer will further aggregate to calculate hourly traffic 
# input log format 
# 125.125.125.125 - uche [20/Jul/2008:12:30:45 +0700] "GET /index.html HTTP/1.1" 200
import sys
import re
ipPattern = re.compile("^\d{3}.\d{1,3}.\d{1,3}.\d{1,3}\s.*$")
#datePattern = re.compile(".*\[\d{1,2}\/\w{3}\/\d{1,4}:\d{1,2}:\d{1,2}\d{1,2}\s+ \+\d{1,4}\]")
monthPattern = re.compile(".*\[\d{1,2}\/(?P<month>\w{3})\/\d{1,4}.*$")
hourPattern = re.compile(".*\[\d{1,2}\/\w{3}\/\d{1,4}:(?P<hour>\d{1,2}):\d{1,2}:\d{1,2}.*")
for line in sys.stdin:
	matched =  hourPattern.match(line)
	print matched.group("hour") + "\t" + "1"
