#!/usr/bin/env python
""" dump 1 """

import sys, json
from struct import *

array=[]

def doit(f):
    chunk = f.read(0x2)
    l0 = unpack('>H', chunk)
    assert l0[0] == 50
    chunk = f.read(l0[0])
    s = unpack('>%ds' % l0[0], chunk)
    chunk = f.read(0x1)
    l2 = unpack('>B', chunk)
    #assert l2[0] == 0
    chunk = f.read(0x2)
    l1 = unpack('>H', chunk)
    #print l1[0] # wotsit ?
    #print l0[0],s[0].decode('utf-16'),l1[0],l2[0]
    #print l0[0],s[0].decode('utf-16'),l1[0]+l2[0]
    #print s[0].decode('utf-16'),l1[0]
    el = {}
    el['name'] = s[0].decode('utf-16')
    el['index'] = l1[0]+l2[0]
    array.append( el )

def doit2(i,f):
  chunk = f.read(0x1)
  o = unpack('>B', chunk)
  assert o[0] == 1
  chunk = f.read(0x1)
  l0 = unpack('>B', chunk)
  chunk = f.read(l0[0])
  s = unpack('>%ds' % l0[0], chunk)
  #print s[0]
  array[i]['value']=s[0]
  array[i]['len']=l0[0]

if __name__ == "__main__":
  filename = sys.argv[1]
  with open(filename,'rb') as f:
    f.seek( 104932524 )
    chunk = f.read(0x2)
    d = unpack('>H', chunk)
    #print d
    assert d[0] == 120
    chunk = f.read(0x2)
    d = unpack('>H', chunk)
    #print d # wotsit ?
    for i in range(0,60):
      doit(f)
    for i in range(1,60):
      array[i]['idxdiff'] = array[i]['index'] - array[i-1]['index']
    chunk = f.read(0x1)
    z = unpack('>B', chunk)
    assert z[0] == 0
    for i in range(0,60):
      doit2(i,f)
  #print array
  print json.dumps(array, sort_keys=True, indent=4)
  
