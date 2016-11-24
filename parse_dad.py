#!/usr/bin/env python
""" parse """

# $ ./parse_dad.py re/pms/merge119_120.dad re/pms/output_016.dad

import sys,re,json,string
from collections import defaultdict

# http://stackoverflow.com/questions/3728655/python-titlecase-a-string-with-exceptions

# @(#)EVMLegacy.dad
def parse_dad_file(filename):
  aFile = open( filename, 'r' )
  lineIter= iter(aFile)
  array=[]
  for linews in lineIter:
    line = linews.strip()
    if not line: continue
    if line.startswith( "/*" ):
      for comws in lineIter:
        com = comws.strip()
        if com.startswith( "*/" ):
          break
    else:
      buf = []
      #name,junk = line.split('{')
      buf.append( line )
      for piimws in lineIter:
        piim = piimws.strip()
        if piim.startswith( "}" ):
          break
        else:
          buf.append( piim )
      #print buf
      # process buf:
      assert len(buf)==4
      clean = [None] * 4
      clean[0] = buf[0].split('{')[0].strip()
      clean[1] = buf[1].strip()
      clean[2] = buf[2].split( '=' )[1].strip()
      clean[3] = buf[3].split( '=' )[1].strip()
      array.append( clean )
  return array

if __name__ == "__main__":
  filename = sys.argv[1] # dict
  filename2 = sys.argv[2]
  res = None
  with open(filename,'r') as f:
    my = re.compile(r'^group = (.+) {\r\n    reservation = (.+)\r\n    recognition = "(.+)"\r\n}', re.MULTILINE)
    #content = f.readlines()
    content = f.read()
    #print content
    res = my.findall( content )
    #print res
  #print len(res)
  #print res
  #print len(res)
  #for it in res:
  #  print 'group = %s {\n    reservation = %s\n    recognition = "%s"\n}' % it
  md = defaultdict(list)
  for it in res:
    # md[1].append('a')
    group, elem, name = it
    assert elem[0:2] == '00'
    key = "%s,%s" % (group, elem[2:4])
    #print key
    md[key].append( name )
  #print md
  #print len(md) # seems to be at least one duplicate !
  """
  res2 = None
  with open(filename2,'r') as f:
    my = re.compile(r'^(.+) {\r\n    (.+)\r\n    dicomVR = (.+)\r\n    dicomVM = (.+)\r\n}', re.MULTILINE)
    content = f.read()
    res2 = my.findall( content )
    #print res2
  """
  res2 = parse_dad_file(filename2)
  #print len(res2)
  #print res2[20]
  array = []
  for it in res2:
    name, tag, vr, vm = it
    key = tag[:-2]
    #print key
    creators = md[ key ]
    #print name
    assert name.startswith( 'DICOM_' ) or name.startswith( 'SPI_' ) or name.startswith( 'ICS_' ) or name.startswith( 'VOL_' ) or name.startswith( 'PIIM_' )
    vnames = name.split('_')
    vclean = [string.capwords(it) for it in vnames]
    if name.startswith( 'DICOM_' ):
      gr,ele = tag.split(',')
      vgr = int( '0x%s' % gr, 16)
      if vgr % 2 == 0:
        assert not creators
        continue
      if not creators:
        #print name
        assert "RESERVATION_OF_GROUP" in name or "LENGTH_OF_GROUP" in name
        continue
      # private attribute
      assert creators
      clean = " ".join(vclean[1:])
    elif name.startswith( 'SPI_' ) or name.startswith( 'ICS_' ):
      if not creators:
        #print tag, name
        assert "RESERVATION_OF_GROUP" in name or "LENGTH_OF_GROUP" in name
        continue
      clean = " ".join(vclean[1:])
    elif name.startswith('VOL_'):
      assert creators
      clean = " ".join(vclean)
    elif name.startswith('PIIM_'):
      print tag
      assert creators
      clean = " ".join(vclean[1:])
    else:
      assert False
    el = {}
    for creator in creators:
      el[ 'creator' ] = creator
      el[ 'name' ] = clean
      el[ 'keyword' ] = name
      el[ 'group' ] = tag[:4]
      el[ 'element' ] = "xx%s" % tag[7:]
      el[ 'vr' ] = vr
      el[ 'vm' ] = vm
      array.append( el )
  #print array
  #for it in array:
  #  #print it
  #  if it['group' ] == '2001' or it['group' ] == '2005':
  #    #print it
  #    print '(%(group)s,%(element)s)\t%(vr)s\t%(keyword)s\t%(vm)s' % it
  print json.dumps(array, sort_keys=True, indent=4)
