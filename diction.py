#!/usr/bin/env python
""" Convert diction.pfl into XML """

import sys

def print_element1( group, element, name, ret ):
  if ret: print '(%s,%s) "%s" (RET)'%(group,element,name)
  else: print '(%s,%s) "%s"'%(group,element,name)

def print_element2( group, element, creator, name, ret ):
  if ret: print '(%s,%s,"%s") "%s" (RET)'%(group,element,creator,name)
  else: print '(%s,%s,"%s") "%s"'%(group,element,creator,name)

retired = "RETIRED"
def process( line ):
  v = line.split(',')
  ret = False
  if len(v) == 5:
    name, group, element, vr, vm = line.split(',')
    if retired in name:
      name = name[:-8]
      ret = True
    print_element1( group, element, name, ret )
  elif len(v) == 6:
    name, group, creator, element, vr, vm = line.split(',')
    print_element2( group, element, creator, name, ret )

if __name__ == "__main__":
  filename = sys.argv[1]
  with open(filename,'rU') as f:
    for line in f:
      line = line.rstrip('\n')
      assert line
      process( line )
