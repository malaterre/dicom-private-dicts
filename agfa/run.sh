#!/bin/sh
set -e
#set -x
./tabula.sh -o "agfa/chunk0.json" --spreadsheet -p 15 -a 400,173,650,1000 "agfa/000978_tcm583-21764.pdf"
./tabula2xml.py  --header "AttributeName,Tag,VR,DefaultValue"  --owner "AGFA"  --files "agfa/chunk0.json" --output "agfa/000978_tcm583-21764_0.xml"
./tabula.sh -o "agfa/chunk0.json" --spreadsheet -p 25 -a 50,61,400,1000 "agfa/000946_tcm583-21755.pdf"
./tabula2xml.py  --header "AttributeName,Tag,VR,Type,DefaultValue,UNK"  --owner "AGFA_ADC_Compact"  --files "agfa/chunk0.json" --output "agfa/000946_tcm583-21755_0.xml"
./tabula.sh -o "agfa/chunk0.json" --spreadsheet -p 16 -a 100,50,250,1000 "agfa/000946_tcm583-21755.pdf"
./tabula2xml.py  --header "AttributeName,Tag,DefaultValue"  --owner "AGFA"  --files "agfa/chunk0.json" --output "agfa/000946_tcm583-21755_1.xml"
./tabula.sh -o "agfa/chunk0.json" --spreadsheet -p 37 -a 291.083,63.878,561.893,547.358 "agfa/000410_tcm583-21790.pdf"
./tabula2xml.py  --header "Tag,VR,VM,AttributeName,Definition"  --owner "1.2.840.113681"  --files "agfa/chunk0.json" --output "agfa/000410_tcm583-21790_0.xml"
rm agfa/chunk?.json
