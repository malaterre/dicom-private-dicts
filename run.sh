#!/bin/sh -x
set -e

TABULA=tabula-0.9.1-jar-with-dependencies.jar

URL=http://www.hitachimed.com/idc/groups/hitachimedical/documents/supportingdocumentpdf/poc_013216.pdf
wget -c $URL

PAGES=58,64

java -jar $TABULA --silent --spreadsheet -f JSON -a 234.647,38.317,794.898,578.479 -p 57 -o data1.json poc_013216.pdf
java -jar $TABULA --silent --spreadsheet -f JSON -p $PAGES -o data2.json poc_013216.pdf
java -jar $TABULA --silent --spreadsheet -f JSON -a 54.686,44.269,123.88,568.807 -p 65 -o data3.json poc_013216.pdf
