#!/usr/bin/env python
import json
import sys
import xmldict

f=sys.argv[1]
#o=sys.argv[2]

with open(f, "rb") as infile:
  i=json.load(infile)


print json.dumps(i, sort_keys=True, indent=4)
