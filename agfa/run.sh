#!/bin/sh
set -e
set -x
./tabula.sh -o "agfa/chunk0.json" -p 15 -a 400,173,650,1000 "agfa/000978_tcm583-21764.pdf"
./tabula2xml.py  --header "AttributeName,Tag,VR,DefaultValue"  --owner "AGFA"  --files "agfa/chunk0.json" --output "agfa/000978_tcm583-21764_0.xml"
