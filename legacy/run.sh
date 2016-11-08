#!/bin/sh -e
set -x
xsltproc merge.xsl index.xml > tmp.xml
xsltproc uniq.xsl tmp.xml > bla.xml
