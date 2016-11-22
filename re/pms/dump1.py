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
AddPadding = False

def doit3(i,f):
  global AddPadding
  """
  chunk = f.read(0x1)
  if AddPadding:
    chunk = f.read(0x1)
  """
  pad = FixPadding[i]['pad']
  chunk = f.read(pad)
  #z = unpack('<B', chunk)
  #print hex(z[0]),z[0]
  #if z[0] != 0:
  #  f.seek(-1,1)
  chunk = f.read(0x2)
  d = unpack('<H', chunk)
  fl = d[0]
  #print pad,hex(f.tell()),hex(fl),fl
  if fl % 2 == 0:
    AddPadding = True
  else:
    AddPadding = False
  chunk = f.read(0x2)
  d = unpack('<H', chunk)
  #print hex(d[0])
  assert d[0] == 0
  chunk = f.read(fl)
  with open("output%d.dad" % i, "w") as text_file:
    text_file.write( chunk[:-2] )

def doit4(i,f):
    chunk = f.read(0x4)
    z = unpack('<I', chunk)
    #print hex(z[0])
    fl = z[0]
    chunk = f.read(fl)
    #print chunk
    #print (f.tell() - 1) % 8

def isnull(instr):
  for c in instr:
    assert ord(c) == 0

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
    #print "debug: %d" % z
    assert z[0] == 0
    for i in range(0,12):
      doit3(i,f)
    # type 4:
    #print hex(f.tell())
    chunk = f.read(0x4)
    z = unpack('<I', chunk)
    assert z[0] == 0
    doit4(0,f)
    # not OK:
    chunk = f.read(0x7)
    isnull(chunk)
    chunk = f.read(0x4)
    z = unpack('<I', chunk)
    fl = z[0]
    chunk = f.read(fl)
    chunk = f.read(0x3)
    isnull(chunk)
    chunk = f.read(0x4)
    z = unpack('<I', chunk)
    fixlen = 0xb06
    print z[0], fl+4+fixlen
    print hex(z[0]), hex(fl+fixlen)
    chunk = f.read(fl+fixlen)
    #print chunk
    # OK:
    chunk = f.read(0x5)
    isnull(chunk)
    doit4(7,f)
    chunk = f.read(0x7)
    isnull(chunk)
    doit4(7,f)
    chunk = f.read(0x3)
    isnull(chunk)
    doit4(8,f)
    doit4(9,f)
    print format(f.tell(), '08x')

  #print array
  #print json.dumps(array, sort_keys=True, indent=4)
  
