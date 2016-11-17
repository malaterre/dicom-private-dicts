#!/usr/bin/env python
""" dump 1 """

import sys
from struct import *

def doit(f):
    chunk = f.read(0x2)
    l0 = unpack('>H', chunk)
    assert l0[0] == 50
    chunk = f.read(l0[0])
    s = unpack('>%ds' % l0[0], chunk)
    chunk = f.read(0x2)
    l1 = unpack('>H', chunk)
    #print l1[0] # wotsit ?
    chunk = f.read(0x1)
    l2 = unpack('>B', chunk)
    assert l2[0] == 0
    print l0[0],s[0],l1[0],l2[0]

def doit2(f):
  chunk = f.read(0x1)
  o = unpack('>B', chunk)
  assert o[0] == 1
  chunk = f.read(0x1)
  l0 = unpack('>B', chunk)
  chunk = f.read(l0[0])
  s = unpack('>%ds' % l0[0], chunk)
  print s[0]

if __name__ == "__main__":
  filename = sys.argv[1]
  with open(filename,'rb') as f:
    f.seek( 104932528 )
    for i in range(0,60):
      doit(f)
    chunk = f.read(0x1)
    z = unpack('>B', chunk)
    assert z[0] == 0
    for i in range(0,60):
      doit2(f)
