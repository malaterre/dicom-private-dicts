#!/usr/bin/env python
import json
import glob

# y will override what is in x
def merge( x, y ):
  ret = dict(x.items() + y.items())
  # now inspect intersection in case value in Y are not OK:
  for key in x.viewkeys() & y.viewkeys():
    if x[key] != y[key]:
      diff = True
      # discard if 'UN'
      if key == 'vr':
        if y[key] == 'UN':
          assert x[key] != 'UN'
          ret[key] = x[key]
          diff = False
        elif x[key] == 'UN':
          # easy case
          diff = False
      elif key == 'name':
        if x[key].title() == y[key].title():
          ret[key] = x[key].title()
          diff = False
        elif x[key].title() in y[key].title():
          # easy case
          diff = False
        elif y[key].title() in x[key].title():
          ret[key] = x[key].title()
          diff = False
      elif key == 'default_value':
        if y[key] in x[key]:
          # easy case
          diff = False
        elif x[key] in y[key]:
          ret[key] = x[key]
          diff = False
      if diff: print 'mismatch: "%s" vs "%s" for entry: %s,%s,%s'% (x[key],y[key],x['group'],x['element'],key)
  #assert( ret == y )
  return ret

result = []
for f in glob.glob("agfa/*.json"):
    if f == "agfa/lists.json": continue
    #print f
    with open(f, "rb") as infile:
        result.append(json.load(infile))

result2 = {}
for owner in result:
  for key,value in owner.items():
    #print key, value
    if not result2.has_key( key ):
      result2[ key ] = {}
    #result2[ key ].add( value )
    res3 = result2[ key ]
    for v in value:
      #print v
      subkey = v['group'],v['element']
      if not res3.has_key( subkey ):
         res3[ subkey ] = v
      else:
         cur = res3[ subkey ]
         res3[ subkey ] = merge( cur, v ) # prefer element v values


#print result2['AGFA']
#json.dumps(result2)

result3 = {}
for key,value in result2.items():
  #print key
  #print value
  result3[ key ] = []
  for subkey,subvalue in value.items():
    result3[ key ].append( subvalue )

with open("merged_file.json", "wb") as outfile:
     json.dump(result3, outfile)
