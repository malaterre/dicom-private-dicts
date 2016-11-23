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

def extract_name(i,f):
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

def isnull(instr):
  for c in instr:
    assert ord(c) == 0

def extract_dad_file(i,f):
  print f.tell()
  corr = 1 # old (orig file)
  corr = 0 # already aligned ???
  assert (f.tell() - corr) % 8 == 0 # 8bytes alignement
  # read length:
  chunk = f.read(0x4)
  z = unpack('<I', chunk)
  fl = z[0]
  chunk = f.read(fl)
  with open("output_%03d.dad" % i, "wb") as binfile:
    binfile.write( chunk )
  # trailing stuff handling:
  pad = (f.tell() - corr) % 8
  if pad != 0:
    chunk = f.read(8 - pad)
    isnull(chunk) # no digital trash, must be an in-memory representation

# the intersting stuff lie in:
# $ dd if=PmsDView.DMP of=dummy2.exe skip=104921721 count=1802240 bs=1
# as a side note we also have:
# $ dd if=PmsDView.DMP of=dummy3.exe skip=106723961 count=1802240 bs=1 
# $ md5sum dummy2.exe dummy3.exe
# 6a58cd8dc039b2cfbeb4529b4fd13106  dummy2.exe
# 6a58cd8dc039b2cfbeb4529b4fd13106  dummy3.exe

if __name__ == "__main__":
  filename = sys.argv[1]
  with open(filename,'rb') as f:
    # MZ starts at 0x640FA79
    #f.seek( 104932524 ) # 0x64124ac # orig file
    f.seek( 0x12F86F3 ) # new
    # file type 1:
    #print "start:", f.tell()
    chunk = f.read(0x2)
    d = unpack('>H', chunk)
    assert d[0] == 120 # number of elements (x2)?
    chunk = f.read(0x2)
    d = unpack('>H', chunk)
    print d # wotsit ?
    assert d[0] == 0x0f00
    for i in range(0,60):
      doit(f)
    chunk = f.read(0x1)
    z = unpack('>B', chunk)
    assert z[0] == 0
    #print (f.tell() - 1) % 4
    for i in range(0,60):
      extract_name(i,f)
    #print "end:", f.tell()
    # file type dad/dotd:
    chunk = f.read(5)
    for i in range(0,153):
      # i > 153 is junk...
      extract_dad_file(i,f)
    print format(f.tell(), '08x')
    chunk = f.read(2000)
    # Some .NET stuff (BSJB)
    # The initials correspond to Brian Harry, Susan Radke-Sproull, Jason
    # Zander, and Bill Evans who were part of the team in 1998 that worked on
    # the CLR.
    with open("general_metadata_header.bin" , "wb") as binfile:
      binfile.write( chunk )

  #print array
  #print json.dumps(array, sort_keys=True, indent=4)
  
