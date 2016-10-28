#! /usr/bin/env python
"""
$ wget http://www.goldbergs.cc/bernie/MRI/DCMVWR/DICT.DAT
"""
import re,os,string


def XMLify(source):
    source = string.replace(source, '&', '&amp;')
    source = string.replace(source, '<', '&lt;')
    source = string.replace(source, '>', '&gt;')
    return source

if __name__ == "__main__":
  #argc = len(os.sys.argv )
  infile = file(os.sys.argv[1], 'r')
  for l in infile.readlines():
    line = l[:-2]
    patt1 = re.compile('^DATA_ELEM\(([0-9A-F]+),\s*([0-9A-F]+),\s*([A-Z][A-Z]),\s*"(.*)"\)(.*)$')
    patt2 = re.compile('^PRIVATE_ELEM\(([0-9A-F]+),\s*([0-9A-F]+),\s*([A-Z][A-Z]),\s*([A-Za-z_0-9]+),\s*"([:A-Z0-9a-z <>/()-]+)"\)(.*)$')
    m1 = patt1.match(line)
    m2 = patt2.match(line)
    if( m1 ):
      #print "ok1",m1.group(1)
      #print line
      #print m1.group(1)
      group = eval( '0x' + m1.group(1) )
      elem  = eval( '0x' + m1.group(2) )
      #print val
      s = '</dict><dict owner="%s">'
      if group % 2:
        if elem < 0xff :
          print s%(m1.group(4))
        else:
          s = '<entry group="%s" element="%s" vr="%s" vm="1" name="%s"/><!-- %s -->'
          print s%(m1.group(1),m1.group(2),m1.group(3),XMLify(m1.group(4)),m1.group(5))
    elif( m2 ):
      s = '<entry group="%s" element="%s" vr="%s" vm="1" name="%s"/><!-- %s -->'
      print s%(m2.group(1),m2.group(2),m2.group(3),XMLify(m2.group(5)),m2.group(6))
    elif (line[0:2] == '//'):
      print "<!-- %s -->"%(line[2:].replace('-','')) # XML and -- are not friend
      #print "<!-- coucou -->"
    else:
      print "error:",line


