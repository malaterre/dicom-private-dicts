#!/usr/bin/env python
"""
Main script to take as input lists.json to generate dependencies
"""
import json
import argparse
import os
import urllib.request, urllib.parse, urllib.error

parser = argparse.ArgumentParser()
parser.add_argument('--dir', help='dir help')
args = parser.parse_args()

def getpdflocalpath(it, dirpath):
  # compute the PDF local path:
  if 'content-disposition' in it:
    pdffile = it['content-disposition']
  else:
    pdffile = os.path.basename(it['url'])
  # use startswith to handle "pdf?nodeid=5148569&vernum=-2"
  assert( pdffile.split('.')[-1].lower().startswith( 'pdf' ) )
  inpdf = "%s/%s" % (dirpath, pdffile)
  return inpdf

dirpath= args.dir
f = os.path.join(dirpath, 'lists.json')
olists = os.path.join(dirpath, 'lists.txt')
orun = os.path.join(dirpath, 'run.sh')
orun2 = os.path.join(dirpath, 'run2.sh')
oxml = os.path.join(dirpath, 'index.xml')
omd5 = os.path.join(dirpath, 'lists.md5')
with open(f) as data_file, open(olists,'w') as out_file, open(orun,'w') as out_file2, open(oxml,'w') as out_file3, open(omd5,'w') as out_file4, open(orun2,'w') as out_file5:
  data = json.load(data_file)
  out_file2.write( '#!/bin/sh\n' )
  out_file2.write( 'set -e\n' )
  out_file2.write( '#set -x\n' )
  # let's write the series of files for this manufacturer in an index file
  out_file3.write( '<index>\n' )
  for it in data:
    if 'url' not in it:
      out_file3.write( '<file>%s/%s</file>\n' % (dirpath,it['xml']) )
      continue
    out_file.write( it['url'] + '\n' )
    inpdf = getpdflocalpath(it, dirpath)
    filename, file_extension = os.path.splitext(inpdf)
    out_file4.write( it['md5'] + '  ' + inpdf + '\n' )
    # loop over each table from this PDF doc:
    # a table has only a single owner for now
    for indext, table in enumerate(it['tables']):
      files=[]
      chunks = table['chunks']
      # a table is split into chunks (basically page or pages-range)
      for index, chunk in enumerate(chunks):
        fil = "%s/%s_%d_%d.json" % (dirpath,it['md5'],indext,index) # md5 clash ?
        files.append( fil )
        # use tabula to extra a single chunk:
        out_file2.write( './scripts/tabula.sh -o "%s" ' % fil )
        # this is nasty on some fuji PDF when only one line is extracted, one need to skip the spreadsheet option:
        if 'spreadsheet' in chunk:
          if chunk['spreadsheet']:
            out_file2.write( "--spreadsheet " )
          else:
            out_file2.write( "--no-spreadsheet " )
        else:
          assert(False) # without explicit option tabula has a random behavior
        # Define as page range (whole page):
        if 'pages' in chunk:
          out_file2.write( "-p " )
          out_file2.write( chunk['pages'] )
        # or a single page (with an area)
        elif 'page' in chunk:
          out_file2.write( "-p " )
          out_file2.write( str(chunk['page']) )
          if 'area' in chunk:
            out_file2.write( " -a " )
            out_file2.write( chunk['area'] )
        else:
          assert(False)
        # compute the target XML file (one per table)
        outxml = "%s_%d.xml" % (filename, indext)
        out_file2.write( ' "%s"' % inpdf )
        out_file2.write( '\n' )
      # now convert the generated JSON into proper XML
      fstr = ','.join(files)
      opts = ""
      # pass the table header (defined manually, generally because JSON output is bogus)
      if "header" in table:
        assert( "use_table_header" not in table or not table["use_table_header"] )
        opts += ' --header "%s" ' % ",".join(table['header'])
      # pass the table owner
      if "owner" in table:
        opts += ' --owner "%s" ' % table['owner']
      # special option to use the table header directly from the JSON generated output
      if "use_table_header" in table and table["use_table_header"]:
        assert( "header" not in table )
        opts += '--use_table_header'
      out_file5.write( './scripts/tabula2xml.py %s --files "%s" --output "%s"\n' % (opts, fstr, outxml) )
      out_file3.write( '<file>%s</file>\n' % urllib.parse.quote(outxml)  )
  out_file2.write( '\n' )
  out_file5.write( '\n' )
  #out_file2.write( '#rm %s/chunk?.json\n' % dirpath )
  out_file3.write( '</index>\n' )
