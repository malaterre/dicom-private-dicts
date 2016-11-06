#!/usr/bin/env python
""" Convert DICT.DAT into JSON """

import json
import sys

creator=None
d={}

def process( line ):
  global creator
  line = line.lstrip() # FIXME some kind of comments may need to be parsed
  #print "DBG1 creator:",creator
  if line[0:2] != '//':
    if line.startswith( 'DATA_ELEM' ):
      line = line[9:]
      line = line.rsplit('\t//',1)[0]
      line = line.rsplit(' //',1)[0]
      line = line.rstrip()
      assert line[0] == '('
      assert line[-1] == ')'
      line = line[1:-1]
      group,element,vr,value = line.split(',',3)
      value = value.strip()[1:-1]
      val = eval("0x%s" % group)
      # DATA_ELEM(3118, 0010, LO, "http://www.gemedicalsystems.com/it_solutions/bamwallthickness/1.0")
      if val == 0x3118:
        # sigh
        group = "3119"
        val = 0x3119
      if val % 2 == 0:
        creator = None
      else:
        vr = vr.strip()
        element = element.strip()
        if element[0:2] == '00':
          assert vr == 'LO'
          assert not "RET" in value
          creator = value
          #print "Found creator:",creator
        else:
          # DATA_ELEM(3113, 1001, SL, "OBSOLETE")
          assert element[0:2] != '00'
          el={}
          el['group'] = group
          el['element'] = element[2:4]
          assert not "RET" in value
          el['name'] = value
          el['vr'] = vr
          el['vm'] = "1"
          assert creator != None
          if not d.has_key( creator ):
            d[ creator ] = []
          d[creator].append( el )
    elif line.startswith( 'PRIVATE_ELEM' ):
      #print line
      line = line[12:]
      assert line[0] == '('
      #line = line.rsplit(')',1)[0]
      line = line.rsplit('\t//',1)[0]
      line = line.rsplit(' //',1)[0]
      line = line.rstrip()
      assert line[0] == '('
      assert line[-1] == ')'
      line = line[1:-1]
      #print line
      group,element,vr,keyword,name = line.split(',',4)
      vr = vr.strip()
      if group == '3118':
        # sigh
        group = "3119"
      el={}
      el['group'] = group
      el['element'] = element[2:4]
      value = name.strip()[1:-1] # remove '"'
      if "(RET)" in value:
        value = value[:-5]
        assert value[-1] == ' '
        value = value[:-1]
        el['retired'] = True
      assert value == value.strip()
      assert not "RET" in value
      #assert not '"' in value
      el['name'] = value
      el['vr'] = vr
      el['vm'] = "1"
      assert creator
      if not d.has_key( creator ):
        d[ creator ] = []
      d[creator].append( el )
    else:
      print line
      assert False
  #print "DBG2 creator:",creator

if __name__ == "__main__":
  filename = sys.argv[1]
  with open(filename,'rU') as f:
    for line in f:
      line = line.rstrip('\n')
      if line != '':
        process( line )
  print json.dumps(d)
