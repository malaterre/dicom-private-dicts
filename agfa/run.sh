#!/bin/sh
set -e
set -x
./tabula.sh -o "agfa/page0.json" -p 24 -a 30,144,370,700 "agfa/000510 DICOM Conformance Statement ADC-QS rev 5.0_tcm583-21763.PDF"
./tabula2xml.py  --header "AttributeName,Tag,VR,DefaultValue"  --files "agfa/page0.json" --output "agfa/000510 DICOM Conformance Statement ADC-QS rev 5.0_tcm583-21763.xml"
./tabula.sh -o "agfa/page0.json" -p 15 -a 400,173,650,1000 "agfa/000978_tcm583-21764.pdf"
./tabula2xml.py  --header "AttributeName,Tag,VR,DefaultValue"  --files "agfa/page0.json" --output "agfa/000978_tcm583-21764.xml"
