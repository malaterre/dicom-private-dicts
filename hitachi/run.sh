#!/bin/sh
set -e
#set -x
./scripts/tabula.sh -o "hitachi/01df924b002f764933bc6566c57fe3ce_0_0.json" --spreadsheet -p 57 -a 234.647,38.317,794.898,578.479 "hitachi/poc_013216.pdf"
./scripts/tabula.sh -o "hitachi/01df924b002f764933bc6566c57fe3ce_0_1.json" --spreadsheet -p 58-64 "hitachi/poc_013216.pdf"
./scripts/tabula.sh -o "hitachi/01df924b002f764933bc6566c57fe3ce_0_2.json" --spreadsheet -p 65 -a 54.686,44.269,123.88,568.807 "hitachi/poc_013216.pdf"
./scripts/tabula.sh -o "hitachi/b7a65104820711efcea3ff699c866065_0_0.json" --spreadsheet -p 57 -a 234.647,38.317,794.898,578.479 "hitachi/echelon-oval-e1e-hm0034-01_dicom_cs_v5_1_r1.pdf"
./scripts/tabula.sh -o "hitachi/b7a65104820711efcea3ff699c866065_0_1.json" --spreadsheet -p 58-64 "hitachi/echelon-oval-e1e-hm0034-01_dicom_cs_v5_1_r1.pdf"
./scripts/tabula.sh -o "hitachi/b7a65104820711efcea3ff699c866065_0_2.json" --spreadsheet -p 65 -a 54.686,44.269,123.88,568.807 "hitachi/echelon-oval-e1e-hm0034-01_dicom_cs_v5_1_r1.pdf"

