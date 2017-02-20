#!/usr/bin/env python

# http://survivalengineer.blogspot.co.uk/2014/04/parsing-pdfs-in-python.html
# so pdfminer seems a much better longer term solution

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

fp = open('miixr0010eac.pdf', 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)

print doc.info  # The "Info" metadata
