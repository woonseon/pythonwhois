#!/usr/bin/python
import pythonwhois
import sys
import json
import re

args = sys.argv[1]
print args

f = open(args,'r')
fw = open('out.txt', 'w')
line = f.readlines()

for i in line:
    a = pythonwhois.get_whois(i)
    b = json.dumps(str(a))
    fw.write(str(b))

print "complete!"

f.close()
fw.close()