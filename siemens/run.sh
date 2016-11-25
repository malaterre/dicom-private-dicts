#!/bin/sh
set -e
#set -x
./tabula.sh -o "siemens/6911efec32a2157fa29ee3237ed89843_0_0.json" --spreadsheet -p 31 -a 363.671,61.359,409.783,535.872 "siemens/acom_pc_rec_dcs_v60-00074270.pdf"
./tabula.sh -o "siemens/6911efec32a2157fa29ee3237ed89843_1_0.json" --spreadsheet -p 32 -a 101.882,60.616,149.482,534.384 "siemens/acom_pc_rec_dcs_v60-00074270.pdf"
./tabula.sh -o "siemens/6911efec32a2157fa29ee3237ed89843_2_0.json" --spreadsheet -p 33 -a 613.594,62.103,670.119,538.847 "siemens/acom_pc_rec_dcs_v60-00074270.pdf"
./tabula.sh -o "siemens/6911efec32a2157fa29ee3237ed89843_3_0.json" --spreadsheet -p 39 -a 544.123,59.872,736.01,540.334 "siemens/acom_pc_rec_dcs_v60-00074270.pdf"
./tabula.sh -o "siemens/c1ed9957d71d5a87368cb91b6c678a00_0_0.json" -p 57 -a 470.093,184.748,721.778,428.018 "siemens/cios_family_dicom_01_16-02589882.pdf"
./tabula.sh -o "siemens/c1ed9957d71d5a87368cb91b6c678a00_1_0.json" -p 58 -a 63.113,189.338,668.228,423.428 "siemens/cios_family_dicom_01_16-02589882.pdf"
./tabula.sh -o "siemens/4fa3996764c1a45e338daf145268d3af_0_0.json" --spreadsheet -p 74 -a 389.458,87.391,759.101,515.047 "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968.pdf"
./tabula.sh -o "siemens/4fa3996764c1a45e338daf145268d3af_1_0.json" --spreadsheet -p 75 -a 74.119,89.622,523.344,518.022 "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968.pdf"
./tabula.sh -o "siemens/4fa3996764c1a45e338daf145268d3af_2_0.json" --spreadsheet -p 75 -a 542.682,87.391,763.576,515.047 "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968.pdf"
./tabula.sh -o "siemens/4fa3996764c1a45e338daf145268d3af_3_0.json" --spreadsheet -p 76 -a 73.387,88.134,399.893,517.278 "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968.pdf"
./tabula.sh -o "siemens/003bdada514adcf773fa1761fa3892b9_0_0.json" --spreadsheet -p 30-43 "siemens/x500_1_0_conformance_statement-00074148.pdf"
#rm siemens/chunk?.json
