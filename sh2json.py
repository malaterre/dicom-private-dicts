#!/usr/bin/env python
# convert a tabula sh script into a partial json representation (copy/paste)
import json
import sys

f=sys.argv[1]

a=[]
with open(f, "r") as ins:
  for line in ins:
    j={}
    array=[]
    items = line.split(" ")
    chunk={}
    assert items[4] == '-a'
    chunk["area"]=items[5]
    assert items[6] == '-p'
    chunk["page"]=items[7]
    array.append(chunk)
    j["chunks"]=array
    #j["header"]=[]
    j["use_table_header"]=True
    j["owner"]="PRIV"
    a.append( j )

print json.dumps(a, sort_keys=True, indent=4)
