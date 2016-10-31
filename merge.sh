#!/bin/sh
set -x
set -e
xsltproc -o agfa.xml    merge.xsl agfa/index.xml
xsltproc -o hitachi.xml merge.xsl hitachi/index.xml

xsltproc -o priv.xml m.xsl empty.xml
