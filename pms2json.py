#!/usr/bin/env python
""" Convert PMS-R32-dict.txt into JSON """

import json
import sys

d={}

def process( line ):
  if line[0] != '#':
    v = line.split('\t')
    assert len(v)==4
    tag,vr,name,vm=v
    group,element=tag.replace('(','').replace(')','').split(',')
    creator = None
    if group == '1001':
      # wotsit ?
      #val = eval(element[0:2])
      print >> sys.stderr, "not handled:", line
    elif group == '2001':
      val = eval(element[0:2])
      if val >= 10 and val <= 15:
        creator = "Philips Imaging DD 00%d" % (val - 10 + 1)
      else:
        print >> sys.stderr, "not handled:", line
    elif group == '2005':
      val = eval(element[0:2])
      assert val >= 10 and val <= 15
      creator = "Philips MR Imaging DD 00%d" % (val - 10 + 1)
    else:
      print group
      assert False
    el={}
    el['group'] = group
    el['element'] = element[2:4]
    el['name'] = name
    el['vr'] = vr
    el['vm'] = vm
    if creator:
      if not d.has_key( creator ):
        d[ creator ] = []
      d[creator].append( el )

if __name__ == "__main__":
  filename = sys.argv[1]
  with open(filename,'rU') as f:
    for line in f:
      line = line.rstrip('\n')
      assert line
      process( line )
  print json.dumps(d)
