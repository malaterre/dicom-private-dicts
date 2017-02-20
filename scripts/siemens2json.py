#!/usr/bin/env python
""" Convert syngo_fV.txt into JSON """

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
  #else: print '(%s,%s) "%s"'%(group,element,name)
  if group == '0051':
    creator = "SIEMENS MR HEADER"
    if not d.has_key( creator ):
      d[ creator ] = []
    d[creator].append( el )
  elif group == '50xx' or group == '60xx':
    # Curve / Overlay
    el = {}
  else:
    #print "[%s]" % group
    val = eval( "0x%s" % group)
    assert val % 2 == 0

def print_element2( group, element, creator, name, vr, vm, ret ):
  el = {}
  el['group'] = group
  el['element'] = element
  el['name'] = name
  el['vr'] = vr
  el['vm'] = vm
  #el['owner'] = creator
  if not d.has_key( creator ):
    d[ creator ] = []
  if ret:
    el['retired'] = True
  #else: print '(%s,%s,"%s") "%s"'%(group,element,creator,name)
  d[creator].append( el )

def process1( line ):
  if line[0] != ';': # discard comment
    group, element, name, vr, vm, sret = line.split('#')
    ret = False
    if sret == 'RET': ret = True
    print_element1( group, element, name, vr, vm, ret )

retired = "RETIRED"

def process2( line ):
  name, group, element, vr, vm = line.split(',')
  ret = False
  if retired in name:
    name = name[:-8]
    ret = True
  print_element1( group, element, name, vr, vm, ret )

def process3( line ):
  name, group, creator, element, vr, vm = line.split(',')
  ret = False
  if retired in name:
    name = name[:-8]
    ret = True
  print_element2( group, element, creator, name, vr, vm, ret )

def process( mode, line ):
  if mode == 0:
    process1( line )
  elif mode == 1:
    process2( line )
  elif mode == 2:
    process3( line )

if __name__ == "__main__":
  filename = sys.argv[1]
  parse = 0
  with open(filename,'rU') as f:
    for line in f:
      line = line.rstrip('\n')
      if line:
        if ord(line[0]) == 0:
          parse += 1
          line = line.lstrip(chr(0))
        process( parse, line )
  print json.dumps(d)
