import codecs
from xml.sax.saxutils import escape

class XMLDictWriter:
  # save as XML (legacy code)
  order=['group','element','vr','vm','name']
  def open(self, filename):
    #with open(oxml,'w') as out_file:
    #with codecs.open(oxml, "w", "utf-8-sig") as out_file:
    self.out_file = codecs.open(filename, "w", "utf-8-sig")
    self.out_file.write( "<dicts>\n" )
  def close(self):
    self.out_file.write( "</dicts>\n" )
  def writeall(self, d):
    new_dict = {}
    for value in d:
      if value['owner'] not in new_dict.keys():
        new_dict[value['owner']] = []
      new_dict[value['owner']].append(value)
    #print new_dict
    for owner,subd in new_dict.items():
      self.writelines(owner, subd)
  def writelines(self, owner, d):
    self.out_file.write( "  <dict " )
    self.out_file.write( 'owner="%s"' % owner )
    self.out_file.write( ">\n" )
    for it in d:
      entry='    <entry'
      #print it.items()
      #for key, value in it.items():
      #  entry += ' %s="%s"' % (key,value)
      for o in self.order:
        #val = '%('+o+')s'
        entry += ' %s="%s"' % (o,escape(it[o]))
      if it.has_key('type'):
        entry += ' type="%s"' % escape(it['type'])
      entry += '>\n'
      if it.has_key('definition'):
        entry += '<definition>'
        entry += escape(it['definition'])
        entry += '</definition>\n'
      if it.has_key('default_value'):
        entry += '<default_value>'
        entry += escape(it['default_value'])
        entry += '</default_value>\n'
      entry += '</entry>\n'
      #print entry
      self.out_file.write( entry )
    self.out_file.write( "</dict>\n" )
