#!/usr/bin/env python
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input help')
parser.add_argument('--lists', help='lists help')
parser.add_argument('--md5', help='output help')
args = parser.parse_args()

f = args.input
olists = args.lists
omd5 = args.lists
with open(f) as data_file:    
  with open(olists,'w') as out_file:
    with open(omd5,'w') as out_file2:
      data = json.load(data_file)
      for it in data:
        url = it['url']
        out_file.write( url )
        out_file.write( '\n' )
        md5 = it['md5']
        out_file2.write( md5 )
        out_file2.write( '\n' )
