#!/bin/sh
set -e
#set -x
./scripts/tabula.sh -o "siemens/6911efec32a2157fa29ee3237ed89843_0_0.json" --spreadsheet -p 31 -a 363.671,61.359,409.783,535.872 "siemens/acom_pc_rec_dcs_v60-00074270.pdf"
./scripts/tabula.sh -o "siemens/6911efec32a2157fa29ee3237ed89843_1_0.json" --spreadsheet -p 32 -a 101.882,60.616,149.482,534.384 "siemens/acom_pc_rec_dcs_v60-00074270.pdf"
./scripts/tabula.sh -o "siemens/6911efec32a2157fa29ee3237ed89843_2_0.json" --spreadsheet -p 33 -a 613.594,62.103,670.119,538.847 "siemens/acom_pc_rec_dcs_v60-00074270.pdf"
./scripts/tabula.sh -o "siemens/6911efec32a2157fa29ee3237ed89843_3_0.json" --spreadsheet -p 39 -a 544.123,59.872,736.01,540.334 "siemens/acom_pc_rec_dcs_v60-00074270.pdf"
./scripts/tabula.sh -o "siemens/c1ed9957d71d5a87368cb91b6c678a00_0_0.json" --no-spreadsheet -p 57 -a 470.093,184.748,721.778,428.018 "siemens/cios_family_dicom_01_16-02589882.pdf"
./scripts/tabula.sh -o "siemens/c1ed9957d71d5a87368cb91b6c678a00_1_0.json" --no-spreadsheet -p 58 -a 63.113,189.338,668.228,423.428 "siemens/cios_family_dicom_01_16-02589882.pdf"
./scripts/tabula.sh -o "siemens/4fa3996764c1a45e338daf145268d3af_0_0.json" --spreadsheet -p 74 -a 389.458,87.391,759.101,515.047 "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968.pdf"
./scripts/tabula.sh -o "siemens/4fa3996764c1a45e338daf145268d3af_1_0.json" --spreadsheet -p 75 -a 74.119,89.622,523.344,518.022 "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968.pdf"
./scripts/tabula.sh -o "siemens/4fa3996764c1a45e338daf145268d3af_2_0.json" --spreadsheet -p 75 -a 542.682,87.391,763.576,515.047 "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968.pdf"
./scripts/tabula.sh -o "siemens/4fa3996764c1a45e338daf145268d3af_3_0.json" --spreadsheet -p 76 -a 73.387,88.134,399.893,517.278 "siemens/fluorospotcompactvf10c_luminosdrfva10c_dcs-00073968.pdf"
./scripts/tabula.sh -o "siemens/003bdada514adcf773fa1761fa3892b9_0_0.json" --spreadsheet -p 30-43 "siemens/x500_1_0_conformance_statement-00074148.pdf"
./scripts/tabula.sh -o "siemens/b44300dadb66e9194dfbd3c78f63ce48_0_0.json" --spreadsheet -p 71 -a 202.742,85.159,233.979,530.666 "siemens/x-leonardo_dcs_vb11-00074288.pdf"
./scripts/tabula.sh -o "siemens/b44300dadb66e9194dfbd3c78f63ce48_1_0.json" --spreadsheet -p 72 -a 88.959,83.672,113.503,536.616 "siemens/x-leonardo_dcs_vb11-00074288.pdf"
./scripts/tabula.sh -o "siemens/b3da02ae5ac369c9f39095cd2c7a4cd5_0_0.json" --no-spreadsheet -p 16 -a 52.785,79.178,727.515,554.243 "siemens/8419009.vft.02-00073814.pdf"
./scripts/tabula.sh -o "siemens/b3da02ae5ac369c9f39095cd2c7a4cd5_1_0.json" --no-spreadsheet -p 17 -a 60.053,85.298,431.078,551.948 "siemens/8419009.vft.02-00073814.pdf"

