#!/usr/bin/env python
import json
import sys
import argparse
import xmldict

f='bla.json'
ref=2
out=[]
with open(f) as data_file:
  pages = json.load(data_file)
  for page in pages:
    data = page['data']
    lineIter = iter(data)
    oldline = None
    for line in lineIter:
      ref_line = line[ref]['text']
      if not ref_line:
        #print "bla"
        if oldline:
          for cellold,cellnew in zip(oldline,line):
            cellold['text'] = ' '.join( [cellold['text'] , cellnew['text']]).rstrip()
      else:
        if oldline:
          out.append( oldline )
        oldline = line
  #print out
print json.dumps(out, sort_keys=True, indent=4)
    #for line in data:
    #  print line[ref]['text']
    #  #for cell in line:
    #  #  print cell['text']
    #  #print line['text']
