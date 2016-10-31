#!/bin/sh -x
set -e

TABULA=tabula-0.9.1-jar-with-dependencies.jar

java -jar $TABULA --silent --spreadsheet -f JSON "$@"
