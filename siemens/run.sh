#!/bin/sh
set -e
#set -x
./tabula.sh -o "siemens/chunk0.json" --spreadsheet -p 31 -a 363.671,61.359,409.783,535.872 "siemens/acom_pc_rec_dcs_v60-00074270.pdf"
./tabula2xml.py  --header "AttributeName,Tag,Type,DefaultValue"  --owner "CARDIO-SMS 1.0"  --files "siemens/chunk0.json" --output "siemens/acom_pc_rec_dcs_v60-00074270_0.xml"
./tabula.sh -o "siemens/chunk0.json" --spreadsheet -p 32 -a 101.882,60.616,149.482,534.384 "siemens/acom_pc_rec_dcs_v60-00074270.pdf"
./tabula2xml.py  --header "AttributeName,Tag,Type,Definition"  --owner "CARDIO-D.R. 1.0"  --files "siemens/chunk0.json" --output "siemens/acom_pc_rec_dcs_v60-00074270_1.xml"
./tabula.sh -o "siemens/chunk0.json" --spreadsheet -p 33 -a 613.594,62.103,670.119,538.847 "siemens/acom_pc_rec_dcs_v60-00074270.pdf"
./tabula2xml.py  --header "AttributeName,Tag,Type,Definition"  --owner "SIEMENS CSA NON-IMAGE"  --files "siemens/chunk0.json" --output "siemens/acom_pc_rec_dcs_v60-00074270_2.xml"
./tabula.sh -o "siemens/chunk0.json" --spreadsheet -p 39 -a 544.123,59.872,736.01,540.334 "siemens/acom_pc_rec_dcs_v60-00074270.pdf"
./tabula2xml.py  --header "AttributeName,Tag,UNK,UNK,Definition"  --owner "CARDIO-D.R. 1.0"  --files "siemens/chunk0.json" --output "siemens/acom_pc_rec_dcs_v60-00074270_3.xml"
./tabula.sh -o "siemens/chunk0.json" -p 57 -a 470.093,184.748,721.778,428.018 "siemens/cios_family_dicom_01_16-02589882.pdf"
./tabula2xml.py  --header "Tag,AttributeName,VR"  --owner "SIEMENS_FLCOMPACT_VA01A_PROC"  --files "siemens/chunk0.json" --output "siemens/cios_family_dicom_01_16-02589882_0.xml"
./tabula.sh -o "siemens/chunk0.json" -p 58 -a 63.113,189.338,668.228,423.428 "siemens/cios_family_dicom_01_16-02589882.pdf"
./tabula2xml.py  --header "Tag,AttributeName,VR"  --owner "SIEMENS_FLCOMPACT_VA01A_PROC"  --files "siemens/chunk0.json" --output "siemens/cios_family_dicom_01_16-02589882_1.xml"
./tabula.sh -o "siemens/chunk0.json" --spreadsheet -p 74 -a 389.458,87.391,759.101,515.047 "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968.pdf"
./tabula2xml.py  --header "Tag,Owner,AttributeName,VR,VM"  --owner "PRIV"  --files "siemens/chunk0.json" --output "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968_0.xml"
./tabula.sh -o "siemens/chunk0.json" --spreadsheet -p 75 -a 74.119,89.622,523.344,518.022 "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968.pdf"
./tabula2xml.py  --header "Tag,Owner,AttributeName,VR,VM"  --owner "PRIV"  --files "siemens/chunk0.json" --output "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968_1.xml"
./tabula.sh -o "siemens/chunk0.json" --spreadsheet -p 75 -a 542.682,87.391,763.576,515.047 "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968.pdf"
./tabula2xml.py  --header "Tag,Owner,AttributeName,VR,VM"  --owner "PRIV"  --files "siemens/chunk0.json" --output "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968_2.xml"
./tabula.sh -o "siemens/chunk0.json" --spreadsheet -p 76 -a 73.387,88.134,399.893,517.278 "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968.pdf"
./tabula2xml.py  --header "Tag,Owner,AttributeName,VR,VM"  --owner "PRIV"  --files "siemens/chunk0.json" --output "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968_3.xml"
rm siemens/chunk?.json
