import codecs
from xml.sax.saxutils import escape

def dumpxml(oxml, owner, d):
  # save as XML (legacy code)
  order=['group','element','vr','vm','name']
  #with open(oxml,'w') as out_file:
  with codecs.open(oxml, "w", "utf-8-sig") as out_file:
    out_file.write( "<dicts>\n" )
    out_file.write( "  <dict " )
    out_file.write( 'owner="%s"' % owner )
    out_file.write( ">\n" )
    for it in d:
      entry='    <entry'
      #print it.items()
      #for key, value in it.items():
      #  entry += ' %s="%s"' % (key,value)
      for o in order:
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
      out_file.write( entry )
    out_file.write( "</dict>\n" )
    out_file.write( "</dicts>\n" )
