#!/usr/bin/env python
""" Convert syngo_fV.txt into XML """

import sys

def print_element1( group, element, name, ret ):
  if ret: print '(%s,%s) "%s" (RET)'%(group,element,name)
  else: print '(%s,%s) "%s"'%(group,element,name)

def print_element2( group, element, creator, name, ret ):
  if ret: print '(%s,%s,"%s") "%s" (RET)'%(group,element,creator,name)
  else: print '(%s,%s,"%s") "%s"'%(group,element,creator,name)

def process1( line ):
  if line[0] != ';': # discard comment
    group, element, name, vr, vm, sret = line.split('#')
    ret = False
    if sret == 'RET': ret = True
    print_element1( group, element, name, ret )

retired = "RETIRED"

def process2( line ):
  name, group, element, vr, vm = line.split(',')
  ret = False
  if retired in name:
    name = name[:-8]
    ret = True
  print_element1( group, element, name, ret )

def process3( line ):
  name, group, creator, element, vr, vm = line.split(',')
  ret = False
  if retired in name:
    name = name[:-8]
    ret = True
  print_element2( group, element, creator, name, ret )

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
          parse = parse + 1
          #print line, ord(line[0])
          line = line.lstrip(chr(0))
          #print line, ord(line[0])
        process( parse, line )
