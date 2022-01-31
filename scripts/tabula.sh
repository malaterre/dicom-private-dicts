#!/bin/sh
set -e

# main driver for the tabula jar
# simply pass option
# only specify the JSON output
# the spreadsheet is driven per client request

TABULA=tabula-1.0.5-jar-with-dependencies.jar

#java -jar $TABULA --silent --spreadsheet -f JSON "$@"

# spreadsheet option is very difficult to handle
# in fact the java code can decide to use the basic or the spreadsheet mode at runtime (depending on???).
# so we need to *always* force one option or the other, without an explicit --spreadsheet or --no-spreadsheet there is no way to control the mode
java -jar $TABULA --silent -f JSON "$@"
