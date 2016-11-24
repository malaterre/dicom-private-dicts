#!/bin/sh
set -e
#set -x
./tabula.sh -o "pms/19df4c2fa6e438dd948e3a6d90ef43f5_0_0.json" --spreadsheet -p 22 -a 254.023,142.0,380.806,529.985 "pms/DICOM_Conformance_Statement_Pegasys_R4.25.pdf?nodeid=5148569&vernum=-2"
./tabula.sh -o "pms/19df4c2fa6e438dd948e3a6d90ef43f5_1_0.json" -p 22 -a 424.034,142.0,530.959,529.985 "pms/DICOM_Conformance_Statement_Pegasys_R4.25.pdf?nodeid=5148569&vernum=-2"
./tabula.sh -o "pms/19df4c2fa6e438dd948e3a6d90ef43f5_2_0.json" -p 22 -a 575.027,142.0,642.237,529.985 "pms/DICOM_Conformance_Statement_Pegasys_R4.25.pdf?nodeid=5148569&vernum=-2"
#rm pms/chunk?.json
