#!/usr/bin/env python
import json
import argparse
import os

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
with open(f) as data_file:    
  with open(olists,'w') as out_file:
    with open(orun,'w') as out_file2:
      data = json.load(data_file)
      for it in data:
        url = it['url']
        out_file.write( url )
        out_file.write( '\n' )
        tables = it['tables']
        files=[]
        for index, table in enumerate(tables):
          fil = "%s/page%d.json" % (dirpath,index)
          files.append( fil )
          out_file2.write( "./tabula.sh -o %s " % fil )
          if table.has_key('pages'):
            out_file2.write( "-p " )
            out_file2.write( table['pages'] )
          elif table.has_key('page'):
            out_file2.write( "-p " )
            out_file2.write( str(table['page']) )
            if table.has_key('area'):
              out_file2.write( " -a " )
              out_file2.write( table['area'] )
          inpdf = "%s/%s" % (dirpath, os.path.basename( it['url']))
          filename, file_extension = os.path.splitext(inpdf)
          outxml = "%s.xml" % filename
          out_file2.write( " %s" % inpdf )
          out_file2.write( '\n' )
        # now convert:
        fstr = ','.join(files)
        opts = ""
        if it.has_key( "opts" ):
          opts = it['opts']
        out_file2.write( "./tabula2xml.py %s --files '%s' --output %s\n" % (opts, fstr, outxml) )
