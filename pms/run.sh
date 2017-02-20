#!/bin/sh
set -e
#set -x
./scripts/tabula.sh -o "pms/19df4c2fa6e438dd948e3a6d90ef43f5_0_0.json" --spreadsheet -p 22 -a 254.023,142.0,386.152,529.985 "pms/DICOM_Conformance_Statement_Pegasys_R4.25.pdf?nodeid=5148569&vernum=-2"
./scripts/tabula.sh -o "pms/19df4c2fa6e438dd948e3a6d90ef43f5_1_0.json" --spreadsheet -p 22 -a 424.034,142.0,535.542,529.985 "pms/DICOM_Conformance_Statement_Pegasys_R4.25.pdf?nodeid=5148569&vernum=-2"
./scripts/tabula.sh -o "pms/19df4c2fa6e438dd948e3a6d90ef43f5_2_0.json" --spreadsheet -p 22 -a 575.027,142.0,646.82,529.985 "pms/DICOM_Conformance_Statement_Pegasys_R4.25.pdf?nodeid=5148569&vernum=-2"
./scripts/tabula.sh -o "pms/f820e4498134b3e0e1150a6c1e72b457_0_0.json" --spreadsheet -p 18 -a 645.278,35.573,738.608,564.188 "pms/DICOM_Conformance_Statement_HDI_5000_R195.xx.pdf?nodeid=5147546&vernum=-2"
./scripts/tabula.sh -o "pms/f820e4498134b3e0e1150a6c1e72b457_1_0.json" --spreadsheet -p 19 -a 52.403,37.868,243.653,559.598 "pms/DICOM_Conformance_Statement_HDI_5000_R195.xx.pdf?nodeid=5147546&vernum=-2"
./scripts/tabula.sh -o "pms/f820e4498134b3e0e1150a6c1e72b457_2_0.json" --spreadsheet -p 20 -a 507.578,36.338,614.678,527.468 "pms/DICOM_Conformance_Statement_HDI_5000_R195.xx.pdf?nodeid=5147546&vernum=-2"

