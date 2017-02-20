#!/bin/sh
set -e
#set -x
./scripts/tabula.sh -o "agfa/258e6887d6b66b92d44d50a7cf4d8a80_0_0.json" --spreadsheet -p 15 -a 400,173,650,1000 "agfa/000978_tcm583-21764.pdf"
./scripts/tabula.sh -o "agfa/ad48c1a03a1e2b6c7e8126c6e42d7870_0_0.json" --spreadsheet -p 25 -a 50,61,400,1000 "agfa/000946_tcm583-21755.pdf"
./scripts/tabula.sh -o "agfa/ad48c1a03a1e2b6c7e8126c6e42d7870_1_0.json" --spreadsheet -p 16 -a 100,50,250,1000 "agfa/000946_tcm583-21755.pdf"
./scripts/tabula.sh -o "agfa/2e52b0254d8591c9839d1f855f08ee35_0_0.json" --spreadsheet -p 37 -a 291.083,63.878,561.893,547.358 "agfa/000410_tcm583-21790.pdf"
./scripts/tabula.sh -o "agfa/35f6dab742c45e9b1afeb13ea6443e39_0_0.json" --no-spreadsheet -p 86 -a 203.509,41.297,554.72,548.767 "agfa/001537_IMPAX_6.7_DICOM_Conformance_Statement.pdf"
./scripts/tabula.sh -o "agfa/5cae2b40cf2c1f5a0c28e448d311766c_0_0.json" --spreadsheet -p 47 -a 188.999,76.269,289.452,520.492 "agfa/001339 NX 2.0.8400-3.0.8400 DICOM Conformance Statement_rev1.1 1.0_tcm586-72224.pdf"
./scripts/tabula.sh -o "agfa/5cae2b40cf2c1f5a0c28e448d311766c_1_0.json" --spreadsheet -p 73 -a 464.685,47.25,722.885,557.696 "agfa/001339 NX 2.0.8400-3.0.8400 DICOM Conformance Statement_rev1.1 1.0_tcm586-72224.pdf"
./scripts/tabula.sh -o "agfa/5cae2b40cf2c1f5a0c28e448d311766c_2_0.json" --spreadsheet -p 74 -a 116.822,49.482,191.976,555.464 "agfa/001339 NX 2.0.8400-3.0.8400 DICOM Conformance Statement_rev1.1 1.0_tcm586-72224.pdf"
./scripts/tabula.sh -o "agfa/5cae2b40cf2c1f5a0c28e448d311766c_3_0.json" --spreadsheet -p 80 -a 657.405,47.25,681.216,569.602 "agfa/001339 NX 2.0.8400-3.0.8400 DICOM Conformance Statement_rev1.1 1.0_tcm586-72224.pdf"

