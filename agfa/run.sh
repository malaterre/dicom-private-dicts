#!/bin/sh
set -e
set -x
./tabula.sh -o "agfa/page0.json" -p 15 -a 400,173,650,1000 "agfa/000978_tcm583-21764.pdf"
./tabula2xml.py  --header "AttributeName,Tag,VR,DefaultValue"  --owner "AGFA"  --files "agfa/page0.json" --output "agfa/000978_tcm583-21764.xml"
./tabula.sh -o "agfa/page0.json" -p 25 -a 50,61,400,1000 "agfa/000946_tcm583-21755.pdf"
./tabula.sh -o "agfa/page1.json" -p 25 -a 50,61,400,1000 "agfa/000946_tcm583-21755.pdf"
./tabula2xml.py  --header "AttributeName,Tag,VR,Type,DefaultValue,UNK"  --owner "AGFA_ADC_Compact"  --files "agfa/page0.json,agfa/page1.json" --output "agfa/000946_tcm583-21755.xml"
