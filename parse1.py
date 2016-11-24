#!/usr/bin/env python
""" parse """

# $ ./parse1.py output_119.dad output_016.dad    

import sys,re,json,string
from collections import defaultdict

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
  res2 = None
  with open(filename2,'r') as f:
    my = re.compile(r'^(.+) {\r\n    (.+)\r\n    dicomVR = (.+)\r\n    dicomVM = (.+)\r\n}', re.MULTILINE)
    content = f.read()
    res2 = my.findall( content )
    #print res2
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
  print json.dumps(array, sort_keys=True, indent=4)
  #for it in array:
  #  #print it
  #  if it['group' ] == '2001' or it['group' ] == '2005':
  #    #print it
  #    print '(%(group)s,%(element)s)\t%(vr)s\t%(keyword)s\t%(vm)s' % it
