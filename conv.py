import json
#from pprint import pprint

with open('data.json') as data_file:    
    pages = json.load(data_file)

#pprint(data)
#print data
#for i in data:
#  print i
#  print "\n"

for page in pages:
  data = page['data']
  #print d
  for j in data:
    #for k in j:
    #print k['text']
    print j[0]['text'],j[1]['text'],j[2]['text'],j[3]['text'].replace('\r',' ')
#    for attribute, value in j.iteritems():
# "      print attribute
#        #print attribute, value # example usage
