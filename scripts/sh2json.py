#!/usr/bin/env python
"""
convert a tabula shell script into a partial json representation (that you can
copy/paste)
"""
import json
import sys

if __name__ == "__main__":
  f=sys.argv[1]
  
  b={}
  b["md5"]="FIXME"
  b["url"]="FIXME"
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
      chunk["spreadsheet"]=True
      array.append(chunk)
      j["chunks"]=array
      #j["header"]=[]
      j["use_table_header"]=True
      j["owner"]="FIXME"
      a.append( j )
  
  b["tables"]=a
  print json.dumps(b, sort_keys=True, indent=4)
