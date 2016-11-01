#!/bin/sh
set -x
set -e

dirs="agfa hitachi fuji"
for dir in $dirs
do
  xsltproc -o $dir.xml    merge.xsl $dir/index.xml
done

xsltproc -o priv.xml m.xsl empty.xml
xsltproc -o private.xml uniq.xsl priv.xml 
