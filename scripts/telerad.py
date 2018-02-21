#!/usr/bin/env python
""" Convert iv.txt ims.txt into JSON """

import json
import sys
#
#public class DDict
#{
#    public static final int tUN = 0;
#    public static final int tUNKNOWN = 0;
#    public static final int tUL = 1;
#    public static final int tUI = 2;
#    public static final int tUS = 3;
#    public static final int tAE = 4;
#    public static final int tAT = 5;
#    public static final int tLO = 6;
#    public static final int tSH = 7;
#    public static final int tOB = 8;
#    public static final int tCS = 9;
#    public static final int tSQ = 10;
#    public static final int tDA = 11;
#    public static final int tTM = 12;
#    public static final int tST = 13;
#    public static final int tPN = 14;
#    public static final int tIS = 15;
#    public static final int tDS = 16;
#    public static final int tAS = 17;
#    public static final int tLT = 18;
#    public static final int tSL = 19;
#    public static final int tFD = 20;
#    public static final int tUS_SS = 21;
#    public static final int tOW_OB = 22;
#    public static final int tSS = 23;
#    public static final int tOW = 24;
#    public static final int tNONE = 25;
#    public static final int tFL = 26;
#    public static final int tUT = 27;
#    public static final int tDT = 28;
#    public static final int tOF = 29;
#    public static final int tUK = 30;
#    public static final int dCommandGroupLength = 0;
#

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

d={}

vrs={}
vrs[0]='UN'
vrs[1]='UL'
vrs[2]='UI'
vrs[3]='US'
vrs[4]='AE'
vrs[5]='AT'
vrs[6]='LO'
vrs[7]='SH'
vrs[8]='OB'
vrs[9]='CS'
vrs[10]='SQ'
vrs[11]='DA'
vrs[12]='TM'
vrs[13]='ST'
vrs[14]='PN'
vrs[15]='IS'
vrs[16]='DS'
vrs[17]='AS'
vrs[18]='LT'
vrs[19]='SL'
vrs[20]='FD'
vrs[21]='US_SS'
vrs[22]='OW_OB'
vrs[23]='SS'
vrs[24]='OW'
vrs[25]='NONE'
vrs[26]='FL'
vrs[27]='UT'
vrs[28]='DT'
vrs[29]='OF'
vrs[30]='UK'

def getvr( ivr ):
  return vrs[ int(ivr) ]


def print_element( group, element, creator, name, vr, vm, ret ):
  el = {}
  el['group'] = group
  el['element'] = element
  el['name'] = name[1:-1]
  el['vr'] = vr
  el['vm'] = vm
  #el['owner'] = creator
  if not d.has_key( creator ):
    d[ creator ] = []
  if ret:
    el['retired'] = True
  #else: print '(%s,%s,"%s") "%s"'%(group,element,creator,name)
  d[creator].append( el )

ims="INTELERAD MEDICAL SYSTEMS"
iv="INTELERAD MEDICAL SYSTEMS INTELEVIEWER"

if __name__ == "__main__":
  creator = iv
  filename = sys.argv[1]
  parse = 0
  with open(filename,'rU') as f:
    for line in f:
      line = line.rstrip('\n')
      group,element,vr,name = line[1:-1].split(',')
      #print hex(int(group)), hex(int(element)), getvr(vr), name
      print_element( "%04x" % int(group.strip()), "%04x" % int(element.strip()), creator, name.strip(), getvr(vr), "1", False )
  print json.dumps(d)
