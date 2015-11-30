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
14:'??', 
14:'UI', 
15:'SS', 
16:'US', 
17:'AT', 
18:'SL', 
19:'??', 
19:'UL', 
20:'FL', 
21:'FD', 
22:'??', 
23:'OB', 
24:'OW', 
25:'??', 
26:'OF', 
27:'SQ', 
}

vm_dict = {
256:'1-n',
257:'1',
258:'1-2',
259:'1-3',
260:'1-4',
261:'1-5',
264:'1-8',
288:'1-32',
355:'1-99',
511:'1-N',
514:'2',
767:'2-N',
771:'3',
1028:'4',
1023:'3-N',
1542:'6',
4112:'16',
}

def process( f ):
  chunk = f.read(8)
  if len(chunk) < 8: sys.exit(0)
  group,element,vrnum,vmnum = unpack('>HHHH', chunk)
  vr = vr_dict[ vrnum ]
  vm = vm_dict[ vmnum ]
  chunk = f.read(0x40)
  name = chunk.rstrip( chr(0) )
  if group % 2 == 1:
    chunk = f.read(0x40+1)
    creator = chunk.rstrip( chr(0) )
    #print '%s,%04X,%s,%02X,%s,%s (%d)' % (name, group,creator, element, vr, vm, vrnum)
    print '%s,%04X,%s,%02X,%s,%s' % (name, group,creator, element, vr, vm )
  else:
    #print '%s,%04X,%04X,%s,%s (%d)' % (name, group, element, vr, vm, vrnum)
    print '%s,%04X,%04X,%s,%s' % (name, group, element, vr, vm)
  #print '%s,%04x,%04x(%d),%d,%d' % (name, group, element,element, vrnum, vmnum)

if __name__ == "__main__":
  filename = sys.argv[1]
  with open(filename,'rb') as f:
    chunk = f.read(0x48)
    #print len(chunk)
    while True:
      process( f )
