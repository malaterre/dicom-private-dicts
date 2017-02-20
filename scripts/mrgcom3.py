#!/usr/bin/env python
""" Convert mrgcom3.dct into XML """

import sys
from struct import *

vr_dict = {
0:'AE',
1:'AS',
2:'CS',
3:'DA',
4:'DS',
5:'DT',
6:'IS',
7:'LO',
8:'LT',
9:'PN',
10:'SH',
11:'ST',
12:'TM',
13:'UT',
14:'UI',
15:'SS',
16:'US',
17:'AT',
18:'SL',
19:'UL',
20:'FL',
21:'FD',
#22:'??',
23:'OB',
24:'OW',
#25:'??',
26:'OF',
27:'SQ',
}

# they encode it like a pair (min,max),
# so 1 is (1,1) = 0x0101
# while 1-99 is 0x0163
vm_dict = {
 256:'0-n', # 0x100
 257:'1',   # 0x101
 258:'1-2',
 259:'1-3',
 260:'1-4',
 261:'1-5',
 264:'1-8',
 288:'1-32',
 355:'1-99',
 511:'1-N',
 514:'2',   # 0x202
 767:'2-N', # 0x2ff
 771:'3',   # 0x303
1023:'3-N', # 0x3ff
1028:'4',   # 0x0404
1542:'6',   # 0x0606
4112:'16',  # 0x1010
}

def vm2string( vmnum ):
  first = vmnum >> 8
  second = vmnum & 0xff
  if first == second:
    ret = str(first)
    return ret
  if first == 0:
    ret = ''
  else:
    ret = str(first) + '-'
  if second == 0xff:
    ret = ret + 'N'
  elif second == 0x0:
    assert first == 0x1
    ret = '0-n'
  else:
    ret = ret + str(second)
  return ret

def process( f ):
  chunk = f.read(8)
  if len(chunk) < 8: sys.exit(0)
  group,element,vrnum,vmnum = unpack('>HHHH', chunk)
  vr = vr_dict[ vrnum ]
  vm = vm_dict[ vmnum ]
  vm2 = vm2string( vmnum )
  #print hex(vmnum),vm, vm2
  assert vm == vm2
  chunk = f.read(0x40)
  name = chunk.rstrip( chr(0) )
  if group % 2 == 1:
    chunk = f.read(0x40+1)
    creator = chunk.rstrip( chr(0) )
    assert creator[0] != chr(0)
    print '%s,%04X,%s,%02X,%s,%s' % (name, group,creator, element, vr, vm )
  else:
    print '%s,%04X,%04X,%s,%s' % (name, group, element, vr, vm)

if __name__ == "__main__":
  filename = sys.argv[1]
  with open(filename,'rb') as f:
    chunk = f.read(0x48)
    while True:
      process( f )
