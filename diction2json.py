#!/usr/bin/env python
""" Convert diction.pfl into JSON """

import json
import sys

d={}

def print_element1( group, element, name, vr, vm, ret ):
  el = {}
  el['group'] = group
  el['element'] = element
  el['name'] = name
  el['vr'] = vr
  el['vm'] = vm
  if ret: el['retired'] = True
  #if ret: print '(%s,%s) "%s" (RET)'%(group,element,name)
  #else: print '(%s,%s) "%s"'%(group,element,name)
  val = eval( "0x%s" % group)
  assert val % 2 == 0

def print_element2( group, element, creator, name, vr, vm, ret ):
  el = {}
  el['group'] = group
  el['element'] = element
  el['name'] = name
  el['vr'] = vr.strip()
  el['vm'] = vm
  #if ret: print '(%s,%s,"%s") "%s" (RET)'%(group,element,creator,name)
  #else: print '(%s,%s,"%s") "%s"'%(group,element,creator,name)
  if not d.has_key( creator ):
    d[ creator ] = []
  if ret:
    el['retired'] = True
  d[creator].append( el )

retired = "RETIRED"
def process( line ):
  v = line.split(',')
  ret = False
  if len(v) == 6 and v[5] == '':
    del v[-1]
  if len(v) == 5:
    name, group, element, vr, vm = v
    if retired in name:
      name = name[:-8]
      ret = True
    print_element1( group, element, name, vr, vm, ret )
  elif len(v) == 6:
    name, group, creator, element, vr, vm = v
    print_element2( group, element, creator, name, vr, vm, ret )

if __name__ == "__main__":
  filename = sys.argv[1]
  with open(filename,'rU') as f:
    for line in f:
      line = line.rstrip('\n')
      assert line
      process( line )
  print json.dumps(d)
