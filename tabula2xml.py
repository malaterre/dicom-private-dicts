#!/usr/bin/env python
import json
import sys
import argparse
#from xml.sax.saxutils import quoteattr
from xml.sax.saxutils import escape

# need to use json output in tabula until:
# https://github.com/tabulapdf/tabula/issues/570

parser = argparse.ArgumentParser()
parser.add_argument('--files', help='dir help')
parser.add_argument('--output', help='dir help')
parser.add_argument('--use_table_header', help='dir help', action='store_true')
parser.add_argument('--header', help='dir help')
parser.add_argument('--owner', help='dir help')
args = parser.parse_args()

debug=False
# we are given a list of files that contains tables to be merged in single dict
files = args.files.split(',')
use_table_header = args.use_table_header
if args.header:
  header = args.header.split(',')

def normalize_header( header ):
  ret = [None] * len(header)
  debug = []
  for index,it in enumerate(header):
    txt = it['text']
    debug.append( txt )
    if txt == 'Attribute Name':
      ret[ index ] = u'AttributeName'
    elif txt == 'Group, Tag':
      ret[ index ] = u'Tag'
    elif txt == 'Default Value':
      ret[ index ] = u'DefaultValue'
    else:
      ret[ index ] = txt
  if(debug): print >> sys.stderr, "debug header:", debug
  return ret

def normalize_entry( entry ):
  ret = {}
  ret['vm'] = '1'
  #if(debug): print entry
  for key,value in entry.items():
    if key == 'VR':
      ret['vr'] = value
    elif key == 'VM':
      ret['vm'] = value
    elif key == 'Tag':
      if(debug): print >> sys.stderr, "debug tag:", value
      group = "0x%s" % value.split(',')[0].replace('(','')
      group = eval(group)
      if( group > 0xffff or group < 0 ):
        raise ValueError, "group issue with %s" % value
      ret['group'] = "%04x" % group
      element = value.split(',')[1].replace(')','')
      if element.startswith( 'xx' ) and len(element) == 4:
        element = element[2:4]
      elif element.startswith( '10' ) and len(element) == 4:
        element = element[2:4]
      elif element.startswith( '0x' ): # usual copy/paste error from editor
        element = element.replace( '0x', '' )
      if element == '00xx' :
        element = '0'
      element = "0x%s" % element
      try:
        element = eval(element)
      except TypeError:
        print "TypeError from input %s" % element
        raise
      if(element > 0xff or element < 0):
        raise ValueError, "element issue with %s" % value
      ret['element'] = "%02x" % element
    elif key == 'AttributeName':
      ret['name'] = value
    elif key == 'Value':
      if value != None and value != '':
        ret['definition'] = value
    elif key == 'DefaultValue':
      if value != None and value != '':
        ret['default_value'] = value
    elif key == 'Type':
      if value != None and value != '':
        ret['type'] = value
    elif key == 'UNK':
      # reserved keyword to indicate skipping of columns
      pass
    else:
      raise ValueError, "impossible key: %s" % key
  return ret

d=[]
for f in files:
  with open(f) as data_file:    
    pages = json.load(data_file)
    for page in pages:
      data = page['data']
      if use_table_header:
        k = normalize_header( data[0] )
        for j in data[1:]:
          elem={}
          elstr=[]
          for el in j:
            elstr.append(el['text'])
          if(debug): print >> sys.stderr, "debug el: %s" % ",".join(elstr)
          for index,col in enumerate(k):
            elem[ col ] = j[index]['text'].replace('\r',' ')
          d.append(normalize_entry(elem))
      elif header:
        k = header
        if(debug): print >> sys.stderr, "debug header:", k
        for j in data[1:]:
          elem={}
          elstr=[]
          for el in j:
            elstr.append(el['text'])
          if(debug): print >> sys.stderr, "debug el: %d/%d -> %s" % (len(k),len(j),",".join(elstr))
          for index,col in enumerate(k):
            elem[ col ] = j[index]['text'].replace('\r',' ')
          d.append(normalize_entry(elem))

# now that dict is complete, save as json:
oxml = args.output
owner = args.owner
order=['group','element','vr','vm','name']
with open(oxml,'w') as out_file:
  #out_file.write( json.dumps(d, sort_keys=True, indent=4) )
  out_file.write( "<dicts>" )
  out_file.write( "<dict " )
  out_file.write( 'owner="%s"' % owner )
  out_file.write( ">" )
  for it in d:
    entry='<entry'
    #print it.items()
    #for key, value in it.items():
    #  entry += ' %s="%s"' % (key,value)
    for o in order:
      #val = '%('+o+')s'
      entry += ' %s="%s"' % (o,escape(it[o]))
    if it.has_key('type'):
      entry += ' type="%s"' % escape(it['type'])
    entry += '>\n'
    if it.has_key('definition'):
      entry += '<definition>'
      entry += it['definition']
      entry += '</definition>\n'
    if it.has_key('default_value'):
      entry += '<default_value>'
      entry += it['default_value']
      entry += '</default_value>\n'
    entry += '</entry>\n'
    #print entry
    out_file.write( entry )
  out_file.write( "</dict>" )
  out_file.write( "</dicts>" )
