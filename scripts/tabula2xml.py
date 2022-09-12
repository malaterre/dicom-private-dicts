#!/usr/bin/env python3
import json
import sys
import argparse
import xmldict

# need to use json output in tabula until:
# https://github.com/tabulapdf/tabula/issues/570

parser = argparse.ArgumentParser()
parser.add_argument('--files', help='dir help')
parser.add_argument('--output', help='dir help')
parser.add_argument('--use_table_header', help='dir help', action='store_true')
parser.add_argument('--header', help='dir help')
parser.add_argument('--owner', help='dir help')
args = parser.parse_args()

debug=True
debug=False
# we are given a list of files that contains tables to be merged in single dict
files = args.files.split(',')
use_table_header = args.use_table_header
header = None
if args.header:
  header = args.header.split(',')
owner = None
if args.owner:
  owner = args.owner

def normalize_header( header ):
  ret = [None] * len(header)
  for index,it in enumerate(header):
    txt = it['text']
    if txt == 'Attribute Name' or txt == 'Name' or txt == 'Attribute':
      ret[ index ] = 'AttributeName'
    elif txt == 'DICOM VR':
      ret[ index ] = 'VR'
    elif txt == 'DICOM VM':
      ret[ index ] = 'VM'
    elif txt == 'DICOM Tag' or txt == 'Group, Tag':
      ret[ index ] = 'Tag'
    elif txt == 'Default Value': # or txt == 'Value':
      ret[ index ] = 'DefaultValue'
    elif txt == 'Description' or txt == 'Attribute Description':
      ret[ index ] = 'Definition'
    elif txt == 'DICOM Private Creator':
      ret[ index ] = 'Owner'
    else:
      ret[ index ] = txt
  if(debug): print("debug header:", debug, ret, file=sys.stderr)
  return ret

def read_group( value ):
  if value.startswith( ">" ):
    value = value[1:].lstrip()
  group = "0x%s" % value.lower()
  try:
    group = eval(group)
  except SyntaxError:
    print("Could not eval group: [%s]" % value)
    return 0
  if( group > 0xffff or group < 0 ):
    raise ValueError("group issue with %s" % value)
  return group

def read_element( value ):
  element = value.replace(' ','').lower();
  if element.startswith( 'xx' ) and len(element) == 4:
    element = element[2:4]
  elif element.startswith( 'yy' ) and len(element) == 4: # sigh
    element = element[2:4]
  elif element.startswith( '10' ) and len(element) == 4:
    element = element[2:4]
  if element.startswith( '0x' ): # usual copy/paste error from editor
    element = element.replace( '0x', '' )
  if len(element) == 4: # typically people use group number, eg: F100
    # Need to handle doc such as 000410_tcm583-21790.pdf
    # where one write '0012' in place of '1012'
    if element == '0010':
      element = '0'
    elif element == '00xx':
      element = '0' # wotsit ?
    elif element == '00yy':
      element = '0' # wotsit ?
    else:
      # FIXME wotsit ?
      element = element[2:4]
    # I need to find the creator !!!
    #return -1
  #if(debug): print >> sys.stderr, "debug element: [%s]/%d"% (element,len(element))
  element = "0x%s" % element
  try:
    element = eval(element)
  except SyntaxError:
    print("SyntaxError from input %s" % element)
    if "..." in value:
      print("accepting as is")
      element = 0
    else:
      raise
  except TypeError:
    print("TypeError from input %s" % element)
    raise
  if(element > 0xff or element < 0):
    raise ValueError("element issue with %s (%d) : %d" % (value, len(value), element))
  return element

def normalize_entry( entry ):
  ret = {}
  ret['vm'] = '1'
  ret['vr'] = 'UN'
  ret['owner'] = owner
  #if(debug): print entry
  for key,value in list(entry.items()):
    if key == 'VR':
      if value != None and value != '':
        ret['vr'] = value
    elif key == 'VM':
      if value != None and value != '':
        ret['vm'] = value.replace(' ','') # really replace '1 - n' into '1-n'
    elif key == 'Tag':
      if(debug): print("debug tag:", value, file=sys.stderr)
      sep = '|'
      if ',' in value:
        sep = ','
      elif ':' in value:
        sep = ':'
      bracko='|'
      brackc='|'
      if '(' in value:
        bracko = '('
        brackc = ')'
      elif '[' in value:
        bracko = '['
        brackc = ']'
      if(debug): print("sep/brack(s) are: [%s]/[%s]/[%s]"% (sep,bracko,brackc), file=sys.stderr)
      v = value.split(sep)
      if len(v) != 2:
        print("Dont know how to split: [%s]"% value)
        return None
      group = read_group( value.split(sep)[0].replace(bracko,'') )
      if( group % 2 == 0 ):
        return None
      ret['group'] = "%04x" % group
      element = read_element( value.split(sep)[1].replace(brackc,'') )
      #if element == -1:
      #  return None
      ret['element'] = "%02x" % element
    elif key == 'AttributeName':
      name = value.replace('\n',' ').strip()
      if name != '' and name[0] == '"' and name[-1] == '"':
        name = name[1:-1]
      ret['name'] = name
    elif key == 'Definition':
      if value != None and value != '':
        ret['definition'] = value
    elif key == 'DefaultValue':
      if value != None and value != '':
        ret['default_value'] = value
    elif key == 'Type':
      if value != None and value != '':
        ret['type'] = value
    elif key == 'Group':
      group = read_group( value )
      if( group % 2 == 0 ):
        return None
      ret['group'] = "%04x" % group
    elif key == 'Element':
      element = read_element( value )
      #if element == -1:
      #  return None
      ret['element'] = "%02x" % element
    elif key == 'Owner':
      if value != None and value != '':
        ret['owner'] = value.replace('\n',' ').strip()
    elif key == 'UNK':
      # reserved keyword to indicate skipping of columns
      pass
    else:
      raise ValueError("impossible key: [%s]" % key)
  if 'name' in ret:
    assert 'vr' in ret
    if ret['vr'] == 'UN' and ret['name'].endswith('Sequence'):
      ret['vr'] = 'SQ'
  return ret

d=[]
for f in files:
  with open(f) as data_file:    
    pages = json.load(data_file)
    for page in pages:
      data = page['data']
      if use_table_header:
        #print data[0]
        k = normalize_header( data[0] )
        #print k
        for j in data[1:]: # skip first line
          elem={}
          elstr=[]
          for el in j:
            elstr.append(el['text'])
          if(debug): print("debug el: %s" % ",".join(elstr).replace('\r',' '), file=sys.stderr)
          for index,col in enumerate(k):
            elem[ col ] = j[index]['text'].replace('\r','\n')
          norm = normalize_entry(elem)
          if norm != None:
            d.append(norm)
      elif header != None:
        k = header
        if(debug): print("debug header: %s"% k, file=sys.stderr)
        for line,j in enumerate(data[0:]): # should I skip the first line ?
          elem={}
          elstr=[]
          for el in j:
            elstr.append(el['text'])
          if(debug): print("debug el: %d/%d -> %s" % (len(k),len(j),",".join(elstr).replace('\r',' ')), file=sys.stderr)
          try:
            for index,col in enumerate(k):
              elem[ col ] = j[index]['text'].replace('\r',' ')
            norm = normalize_entry(elem)
            if norm != None:
              d.append(norm)
          except IndexError:
            jointed = ",".join(elstr)
            if line == 0 or ('Tag' in jointed or 'Attribute' in jointed or 'Notes' in jointed and line == 1):
              print("Pb with table header: %s" % ",".join(elstr))
            else:
              print("Pb with line %d: %s %s" % (line,",".join(elstr),",".join(header)))
              raise
      else:
        assert(False)

oxml = args.output

w = xmldict.XMLDictWriter()
w.open(oxml)
#w.writelines(owner, d)
w.writeall(d)
w.close()
