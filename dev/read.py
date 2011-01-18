#!/usr/bin/python
import re
f = open("three-rec.txt", "r")
j = 0
read = f.read()
buf = []

for i in read.split('\n'):
    if(re.match("([A-Za-z]+)\s+(\d+)", i)):
        a = re.match("([A-Za-z]+)\s+(\d+)", i).group(1)
        b = re.match("([A-Za-z]+)\s+(\d+)", i).group(2)
        buf.append((a,int(b)))
        j = j +1
sorted = sorted(buf, key=lambda bufs: bufs[1])

for i in sorted:
    if(i[1] > 4):
        print "%s %s" % (i[0].lower(),i[1])
