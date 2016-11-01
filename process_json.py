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
        # let's write the series of files for this manufacturer in an index file
        out_file3.write( '<index>\n' )
        for it in data:
          url = it['url']
          out_file.write( url )
          out_file.write( '\n' )
          tables = it['tables']
          # loop over each table from this PDF doc:
          # a table has only a single owner for now
          for indext, table in enumerate(tables):
            files=[]
            chunks = table['chunks']
            # a table is split into chunks (basically page or pages-range)
            for index, chunk in enumerate(chunks):
              fil = "%s/chunk%d.json" % (dirpath,index)
              files.append( fil )
              # use tabula to extra a single chunk:
              out_file2.write( './tabula.sh -o "%s" ' % fil )
              # Define as page range (whole page):
              if chunk.has_key('pages'):
                out_file2.write( "-p " )
                out_file2.write( chunk['pages'] )
              # or a single page (with an area)
              elif chunk.has_key('page'):
                out_file2.write( "-p " )
                out_file2.write( str(chunk['page']) )
                if chunk.has_key('area'):
                  out_file2.write( " -a " )
                  out_file2.write( chunk['area'] )
              else:
                assert(False)
              # compute the PDF local path:
              inpdf = "%s/%s" % (dirpath, os.path.basename( it['url']))
              filename, file_extension = os.path.splitext(inpdf)
              # compute the target XML file (one per table)
              outxml = "%s_%d.xml" % (filename, indext)
              out_file2.write( ' "%s"' % inpdf )
              out_file2.write( '\n' )
            # now convert the generated JSON into proper XML
            fstr = ','.join(files)
            opts = ""
            # pass the table header (defined manually, generally because JSON output is bogus)
            if table.has_key( "header" ):
              assert( not table.has_key( "opts" ) )
              opts += ' --header "%s" ' % ",".join(table['header'])
            # pass the table owner
            if table.has_key( "owner" ):
              opts += ' --owner "%s" ' % table['owner']
            # special option to use the table header directly from the JSON generated output
            if table.has_key( "opts" ):
              opts += table['opts']
            out_file2.write( './tabula2xml.py %s --files "%s" --output "%s"\n' % (opts, fstr, outxml) )
            out_file3.write( '<file>%s</file>\n' % urllib.quote(outxml)  )
        out_file3.write( '</index>\n' )
