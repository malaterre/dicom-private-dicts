#!/usr/bin/env python
""" Convert syngo_fV.txt into XML """

import sys

def print_element( group, element, creator, name ):
  if creator: print '(%s,%s,"%s") %s'%(group,element,creator,name)
  else: print "(%s,%s) %s"%(group,element,name)

def process_public( line ):
  name, group, element, vr, vm, ret = line.split('#')
  creator = None
  print_element( group, element, creator, name )

ret = "RETIRED"

def process_private( line ):
  v = line.split(',')
  if len(v) == 5:
    name, group, element, vr, vm = line.split(',')
    creator = None
  elif len(v) == 6:
    name, group, creator, element, vr, vm = line.split(',')
    if ret in name: name = name[:-8]
  else:
    assert None
  print_element( group, element, creator, name )

if __name__ == "__main__":
  filename= sys.argv[1]
  with open(filename,'rU') as f:
    for line in f:
      line = line.rstrip('\n')
      if line and line[0] != ';': # discard comment
        if '#' in line: process_public( line )
        else: process_private( line )
