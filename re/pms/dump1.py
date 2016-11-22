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

FixPadding = [
 { 'pad' : 1 },
 { 'pad' : 1 },
 { 'pad' : 1 },
 { 'pad' : 2 },
 { 'pad' : 0 },
 { 'pad' : 6 },
 { 'pad' : 2 },
 { 'pad' : 1 },
 { 'pad' : 7 },
 { 'pad' : 4 },
 { 'pad' : 4 },
 { 'pad' : 3 },
]

def isnull(instr):
  for c in instr:
    assert ord(c) == 0

def doit3(i,f):
  pad = FixPadding[i]['pad']
  #print f.tell(), pad, f.tell() // 8, f.tell() % 8
  chunk = f.read(pad)
  #print f.tell(), pad, (f.tell() - 1 ) % 8
  assert (f.tell() - 1) % 8 == 0 # seems like to 8 bytes aligned...
  isnull(chunk)
  chunk = f.read(0x4)
  d = unpack('<I', chunk)
  fl = d[0]
  chunk = f.read(fl)
  with open("output%d.dad" % i, "w") as text_file:
    text_file.write( chunk[:-2] )

def doit4(i,f,fixlen = 0):
  assert (f.tell() - 1) % 8 == 0 # 8bytes alignement
  chunk = f.read(0x4)
  z = unpack('<I', chunk)
  fl = z[0] + fixlen
  chunk = f.read(fl)
  #if i == 140:
  #  print fl
  #  #print chunk

def doit5(i,f):
  pad = (f.tell() - 1) % 8
  if pad != 0:
    chunk = f.read(8 - pad)
    isnull(chunk)
  doit4(i,f)
  

if __name__ == "__main__":
  filename = sys.argv[1]
  with open(filename,'rb') as f:
    f.seek( 104932524 ) # 0x64124ac
    # file type 1:
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
    # file type 2:
    chunk = f.read(0x4)
    z = unpack('<I', chunk)
    assert z[0] == 0
    for i in range(0,12):
      doit3(i,f)
    # file type 4:
    chunk = f.read(0x4)
    z = unpack('<I', chunk)
    assert z[0] == 0
    # first one OK
    doit4(0,f)
    # not OK:
    chunk = f.read(0x7)
    isnull(chunk)
    doit4(1,f)
    #print chunk
    chunk = f.read(0x3)
    isnull(chunk)
    doit4(2,f,235)
    # OK:
    for i in range(3,140):
      # i >= 140 is junk...
      doit5(i,f)
    print format(f.tell(), '08x')

  #print array
  #print json.dumps(array, sort_keys=True, indent=4)
  
