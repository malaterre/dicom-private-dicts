#!/bin/sh
set -e

TABULA=tabula-0.9.1-jar-with-dependencies.jar

#java -jar $TABULA --silent --spreadsheet -f JSON "$@"
java -jar $TABULA --silent -f JSON "$@"
