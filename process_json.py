#!/usr/bin/env python
import json
import argparse
import os
import urllib

parser = argparse.ArgumentParser()
parser.add_argument('--dir', help='dir help')
#parser.add_argument('--input', help='input help')
#parser.add_argument('--lists', help='lists help')
#parser.add_argument('--md5', help='output help')
#parser.add_argument('--run', help='run help')
args = parser.parse_args()

dirpath= args.dir
f = os.path.join(dirpath, 'lists.json')
olists = os.path.join(dirpath, 'lists.txt')
orun = os.path.join(dirpath, 'run.sh')
oxml = os.path.join(dirpath, 'index.xml')
with open(f) as data_file:    
  with open(olists,'w') as out_file:
    with open(orun,'w') as out_file2:
      with open(oxml,'w') as out_file3:
        data = json.load(data_file)
        out_file2.write( '#!/bin/sh\n' )
        out_file2.write( 'set -e\n' )
        out_file2.write( 'set -x\n' )
        out_file3.write( '<index>\n' )
        for it in data:
          url = it['url']
          out_file.write( url )
          out_file.write( '\n' )
          tables = it['tables']
          for indexold, table in enumerate(tables):
            files=[]
            chunks = table['chunks']
            for index, chunk in enumerate(chunks):
              fil = "%s/table%d.json" % (dirpath,index)
              files.append( fil )
              out_file2.write( './tabula.sh -o "%s" ' % fil )
              if chunk.has_key('pages'):
                out_file2.write( "-p " )
                out_file2.write( chunk['pages'] )
              elif chunk.has_key('page'):
                out_file2.write( "-p " )
                out_file2.write( str(chunk['page']) )
                if chunk.has_key('area'):
                  out_file2.write( " -a " )
                  out_file2.write( chunk['area'] )
              inpdf = "%s/%s" % (dirpath, os.path.basename( it['url']))
              filename, file_extension = os.path.splitext(inpdf)
              outxml = "%s_%d.xml" % (filename, indexold)
              out_file2.write( ' "%s"' % inpdf )
              out_file2.write( '\n' )
            # now convert:
            fstr = ','.join(files)
            opts = ""
            if table.has_key( "header" ):
              assert( not table.has_key( "opts" ) )
              opts += ' --header "%s" ' % ",".join(table['header'])
            if table.has_key( "owner" ):
              opts += ' --owner "%s" ' % table['owner']
            if table.has_key( "opts" ):
              opts += table['opts']
            out_file2.write( './tabula2xml.py %s --files "%s" --output "%s"\n' % (opts, fstr, outxml) )
            out_file3.write( '<file>%s</file>\n' % urllib.quote(outxml)  )
        out_file3.write( '</index>\n' )
