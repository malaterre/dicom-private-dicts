#!/bin/sh
set -e
#set -x
./tabula.sh -o "pms/19df4c2fa6e438dd948e3a6d90ef43f5_0_0.json" --spreadsheet -p 22 -a 254.023,142.0,386.152,529.985 "pms/DICOM_Conformance_Statement_Pegasys_R4.25.pdf?nodeid=5148569&vernum=-2"
./tabula.sh -o "pms/19df4c2fa6e438dd948e3a6d90ef43f5_1_0.json" --spreadsheet -p 22 -a 424.034,142.0,535.542,529.985 "pms/DICOM_Conformance_Statement_Pegasys_R4.25.pdf?nodeid=5148569&vernum=-2"
./tabula.sh -o "pms/19df4c2fa6e438dd948e3a6d90ef43f5_2_0.json" --spreadsheet -p 22 -a 575.027,142.0,646.82,529.985 "pms/DICOM_Conformance_Statement_Pegasys_R4.25.pdf?nodeid=5148569&vernum=-2"
#rm pms/chunk?.json
