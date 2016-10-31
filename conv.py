#try:
#    import simplejson as json
#except ImportError:
#    import json
import json
#from pprint import pprint

# need to use json output in tabula until:
# https://github.com/tabulapdf/tabula/issues/570

#files = [ 'data1.json', 'data2.json', 'data3.json']
files = [ '/tmp/foo.json']

d=[]
for f in files:
  with open(f) as data_file:    
      pages = json.load(data_file)
  
  #pprint(pages)
  #print data
  #for i in data:
  #  print i
  #  print "\n"
  
  for page in pages:
    data = page['data']
    #print data.__class__
    #print "header:", data[0]
    k = data[0]
    #print "header:",k[0]['text'],k[1]['text'],k[2]['text'],k[3]['text']
    for j in data[1:]:
      #for k in j:
      #print k['text']
      #print j[0]['text'],j[1]['text'],j[2]['text'],j[3]['text'].replace('\r',' ')
      elem={}
      elem[ k[0]['text'] ] = j[0]['text']
      elem[ k[1]['text'] ] = j[1]['text']
      elem[ k[2]['text'] ] = j[2]['text']
      elem[ k[3]['text'] ] = j[3]['text'].replace('\r',' ')
      d.append(elem)
  #    for attribute, value in j.iteritems():
  # "      print attribute
  #        #print attribute, value # example usage
  
  #print d
print json.dumps(d)
