#!/usr/bin/env python
import json
import sys
import xmldict

f=sys.argv[1]
o=sys.argv[2]

with open(f, "rb") as infile:
  i=json.load(infile)

w = xmldict.XMLDictWriter()
w.open(o)
for key,values in i.items():
  w.writelines(key,values)
w.close()
