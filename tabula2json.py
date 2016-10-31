#!/usr/bin/env python
import json
import argparse

# need to use json output in tabula until:
# https://github.com/tabulapdf/tabula/issues/570

parser = argparse.ArgumentParser()
parser.add_argument('--files', help='dir help')
parser.add_argument('--output', help='dir help')
parser.add_argument('--use_table_header', help='dir help')
args = parser.parse_args()

# we are given a list of files that contains tables to be merged in single dict
files = args.files.split(',')

def normalize_header( header ):
  ret = [None] * len(header)
  for index,it in enumerate(header):
    txt = it['text']
    if txt == 'Attribute Name':
      ret[ index ] = u'AttributeName'
    else:
      ret[ index ] = txt
  return ret

d=[]
for f in files:
  with open(f) as data_file:    
    pages = json.load(data_file)
    for page in pages:
      data = page['data']
      numcol = len( data[0] )
      k = normalize_header( data[0] )
      for j in data[1:]:
        elem={}
        for index,col in enumerate(k):
          elem[ col ] = j[index]['text'].replace('\r',' ')
        #elem[ k[0] ] = j[0]['text']
        #elem[ k[1] ] = j[1]['text']
        #elem[ k[2] ] = j[2]['text']
        #elem[ k[3] ] = j[3]['text'].replace('\r',' ')
        d.append(elem)

# now that dict is complete, save as json:
ojson = args.output
with open(ojson,'w') as out_file:
  out_file.write( json.dumps(d, sort_keys=True, indent=4) )
