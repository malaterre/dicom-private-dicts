#!/usr/bin/env python
import json
import argparse

# need to use json output in tabula until:
# https://github.com/tabulapdf/tabula/issues/570

parser = argparse.ArgumentParser()
parser.add_argument('--files', help='dir help')
parser.add_argument('--output', help='dir help')
parser.add_argument('--use_table_header', help='dir help', action='store_true')
parser.add_argument('--header', help='dir help')
args = parser.parse_args()

# we are given a list of files that contains tables to be merged in single dict
files = args.files.split(',')
use_table_header = args.use_table_header

def normalize_header( header ):
  ret = [None] * len(header)
  for index,it in enumerate(header):
    txt = it['text']
    if txt == 'Attribute Name':
      ret[ index ] = u'AttributeName'
    else:
      ret[ index ] = txt
  return ret

def normalize_entry( entry ):
  ret = {}
  ret['vm'] = 1
  for key,value in entry.items():
    if key == 'VR':
      ret['vr'] = value
    elif key == 'VM':
      ret['vm'] = value
    elif key == 'Tag':
      ret['group'] = value.split(',')[0].replace('(','')
      ret['element'] = value.split(',')[1].replace(')','').replace('xx','')
    elif key == 'AttributeName':
      ret['name'] = value
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
          for index,col in enumerate(k):
            elem[ col ] = j[index]['text'].replace('\r',' ')
          d.append(normalize_entry(elem))

# now that dict is complete, save as json:
oxml = args.output
with open(oxml,'w') as out_file:
  #out_file.write( json.dumps(d, sort_keys=True, indent=4) )
  out_file.write( "<dicts>" )
  out_file.write( "<dict>" )
  for it in d:
    entry='<entry'
    #print it.items()
    for key, value in it.items():
      entry += ' %s="%s"' % (key,value)
    entry += '>\n'
    #print entry
    out_file.write( entry )
  out_file.write( "</dict>" )
  out_file.write( "</dicts>" )
