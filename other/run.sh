#!/bin/sh
set -e
#set -x
./tabula.sh -o "other/chunk0.json" --spreadsheet -p 24 -a  274.253,76.118,373.703,538.178 "other/DicomClient_Conformance_35.pdf"
./tabula2xml.py  --owner "SCHICK TECHNOLOGIES - Viewset Creator ID" --use_table_header --files "other/chunk0.json" --output "other/DicomClient_Conformance_35_0.xml"
./tabula.sh -o "other/chunk0.json" --spreadsheet -p 24 -a  400.478,80.708,675.113,536.648 "other/DicomClient_Conformance_35.pdf"
./tabula2xml.py  --owner "SCHICK TECHNOLOGIES - Viewset Item Creator ID" --use_table_header --files "other/chunk0.json" --output "other/DicomClient_Conformance_35_1.xml"
./tabula.sh -o "other/chunk0.json" --spreadsheet -p 25 -a  179.393,79.178,242.123,536.648 "other/DicomClient_Conformance_35.pdf"
./tabula2xml.py  --owner "SCHICK TECHNOLOGIES - Change List Creator ID" --use_table_header --files "other/chunk0.json" --output "other/DicomClient_Conformance_35_2.xml"
./tabula.sh -o "other/chunk0.json" --spreadsheet -p 25 -a  271.193,79.943,366.053,537.413 "other/DicomClient_Conformance_35.pdf"
./tabula2xml.py  --owner "SCHICK TECHNOLOGIES - Change Item Creator ID" --use_table_header --files "other/chunk0.json" --output "other/DicomClient_Conformance_35_3.xml"
./tabula.sh -o "other/chunk0.json" --spreadsheet -p 25 -a  490.748,77.648,555.008,539.708 "other/DicomClient_Conformance_35.pdf"
./tabula2xml.py  --owner "SCHICK TECHNOLOGIES - Note List Creator ID" --use_table_header --files "other/chunk0.json" --output "other/DicomClient_Conformance_35_4.xml"
./tabula.sh -o "other/chunk0.json" --spreadsheet -p 25 -a  580.253,74.588,680.468,536.648 "other/DicomClient_Conformance_35.pdf"
./tabula2xml.py  --owner "SCHICK TECHNOLOGIES - Note Item Creator ID" --use_table_header --files "other/chunk0.json" --output "other/DicomClient_Conformance_35_5.xml"
./tabula.sh -o "other/chunk0.json" --spreadsheet -p 26 -a  175.568,79.178,221.468,534.353 "other/DicomClient_Conformance_35.pdf"
./tabula2xml.py  --owner "SCHICK TECHNOLOGIES - Image Security Creator ID" --use_table_header --files "other/chunk0.json" --output "other/DicomClient_Conformance_35_6.xml"
./tabula.sh -o "other/chunk0.json" --spreadsheet -p 15 -a 198.518,53.168,708.773,568.778 "other/DICOMconformanceTruDR_VPACSv15.pdf"
./tabula.sh -o "other/chunk1.json" --spreadsheet -p 16 -a 63.878,53.168,386.708,558.068 "other/DICOMconformanceTruDR_VPACSv15.pdf"
./tabula2xml.py  --header "AttributeName,Tag,VR,Type,Definition"  --owner "Sound Technologies"  --files "other/chunk0.json,other/chunk1.json" --output "other/DICOMconformanceTruDR_VPACSv15_0.xml"
rm other/chunk?.json