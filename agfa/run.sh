#!/bin/sh
set -e
#set -x
./tabula.sh -o "agfa/258e6887d6b66b92d44d50a7cf4d8a80_0_0.json" --spreadsheet -p 15 -a 400,173,650,1000 "agfa/000978_tcm583-21764.pdf"
./tabula.sh -o "agfa/ad48c1a03a1e2b6c7e8126c6e42d7870_0_0.json" --spreadsheet -p 25 -a 50,61,400,1000 "agfa/000946_tcm583-21755.pdf"
./tabula.sh -o "agfa/ad48c1a03a1e2b6c7e8126c6e42d7870_1_0.json" --spreadsheet -p 16 -a 100,50,250,1000 "agfa/000946_tcm583-21755.pdf"
./tabula.sh -o "agfa/2e52b0254d8591c9839d1f855f08ee35_0_0.json" --spreadsheet -p 37 -a 291.083,63.878,561.893,547.358 "agfa/000410_tcm583-21790.pdf"
#rm agfa/chunk?.json
