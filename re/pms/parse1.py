#!/usr/bin/env python
""" parse """

# $ ./parse1.py output_119.dad output_016.dad    

import sys,re,json
from collections import defaultdict

if __name__ == "__main__":
  filename = sys.argv[1] # dict
  filename2 = sys.argv[2]
  res = None
  with open(filename,'r') as f:
    my = re.compile(r'^group = (.+) {\r\n    reservation = (.+)\r\n    recognition = "(.+)"\r\n}', re.MULTILINE)
    #content = f.readlines()
    content = f.read()
    #print content
    res = my.findall( content )
    #print res
  #print len(res)
  #print res[0]
  md = defaultdict(list)
  for it in res:
    # md[1].append('a')
    group, elem, name = it
    assert elem[0:2] == '00'
    key = "%s,%s" % (group, elem[2:4])
    #print key
    md[key] = name
  #print md
  #print len(md)
  res2 = None
  with open(filename2,'r') as f:
    my = re.compile(r'^(.+) {\r\n    (.+)\r\n    dicomVR = (.+)\r\n    dicomVM = (.+)\r\n}', re.MULTILINE)
    content = f.read()
    res2 = my.findall( content )
    #print res2
  #print len(res2)
  #print res2[20]
  array = []
  for it in res2:
    name, tag, vr, vm = it
    key = tag[:-2]
    #print key
    creator = md[ key ]
    el = {}
    el[ 'creator' ] = creator
    el[ 'name' ] = name
    el[ 'group' ] = tag[:4]
    el[ 'element' ] = "xx%s" % tag[7:]
    el[ 'vr' ] = vr
    el[ 'vm' ] = vm
    array.append( el )
  #print array
  print json.dumps(array, sort_keys=True, indent=4)
