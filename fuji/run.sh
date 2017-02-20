#!/bin/sh
set -e
#set -x
./scripts/tabula.sh -o "fuji/d31bc8d4526b877bc4e117a91d928dfc_0_0.json" --spreadsheet -p 27-30 "fuji/FCR-Go-Flash-IIP.pdf"
./scripts/tabula.sh -o "fuji/d31bc8d4526b877bc4e117a91d928dfc_0_1.json" --spreadsheet -p 31 -a 0,0,450,1000 "fuji/FCR-Go-Flash-IIP.pdf"
./scripts/tabula.sh -o "fuji/d31bc8d4526b877bc4e117a91d928dfc_1_0.json" --spreadsheet -p 38 -a 427.714,30.122,778.021,538.847 "fuji/FCR-Go-Flash-IIP.pdf"
./scripts/tabula.sh -o "fuji/d31bc8d4526b877bc4e117a91d928dfc_1_1.json" --spreadsheet -p 39 -a 75.932,59.872,498.382,562.647 "fuji/FCR-Go-Flash-IIP.pdf"
./scripts/tabula.sh -o "fuji/ffe64d981344b2895d8a2c405d74ae2a_0_0.json" --spreadsheet -p 24 -a 161.033,130.433,262.013,498.398 "fuji/qa-ws771_dcs.pdf"
./scripts/tabula.sh -o "fuji/ffe64d981344b2895d8a2c405d74ae2a_0_1.json" --spreadsheet -p 24 -a 263.543,116.663,449.438,506.813 "fuji/qa-ws771_dcs.pdf"
./scripts/tabula.sh -o "fuji/ffe64d981344b2895d8a2c405d74ae2a_0_2.json" --spreadsheet -p 24 -a 450.203,94.478,643.748,500.693 "fuji/qa-ws771_dcs.pdf"
./scripts/tabula.sh -o "fuji/ffe64d981344b2895d8a2c405d74ae2a_0_3.json" --spreadsheet -p 24 -a 645.278,117.428,716.423,520.583 "fuji/qa-ws771_dcs.pdf"
./scripts/tabula.sh -o "fuji/ffe64d981344b2895d8a2c405d74ae2a_0_4.json" --spreadsheet -p 25 -a 86.828,119.723,200.813,515.227 "fuji/qa-ws771_dcs.pdf"
./scripts/tabula.sh -o "fuji/90fe6f0ec69a1caa154858b36a04453a_0_0.json" --spreadsheet -p 27 -a 431.843,130.433,717.188,500.693 "fuji/HI-C655.pdf"
./scripts/tabula.sh -o "fuji/90fe6f0ec69a1caa154858b36a04453a_0_1.json" --spreadsheet -p 28 -a 88.358,131.963,294.143,503.753 "fuji/HI-C655.pdf"
./scripts/tabula.sh -o "fuji/90fe6f0ec69a1caa154858b36a04453a_0_2.json" --no-spreadsheet -p 28 -a 295.673,130.433,306.383,501.458 "fuji/HI-C655.pdf"
./scripts/tabula.sh -o "fuji/90fe6f0ec69a1caa154858b36a04453a_0_3.json" --spreadsheet -p 28 -a 307.913,133.493,465.503,496.103 "fuji/HI-C655.pdf"
./scripts/tabula.sh -o "fuji/90fe6f0ec69a1caa154858b36a04453a_0_4.json" --spreadsheet -p 28 -a 522.112,125.078,563.423,498.398 "fuji/HI-C655.pdf"
./scripts/tabula.sh -o "fuji/90fe6f0ec69a1caa154858b36a04453a_0_5.json" --no-spreadsheet -p 28 -a 564.953,128.137,576.428,493.043 "fuji/HI-C655.pdf"
./scripts/tabula.sh -o "fuji/90fe6f0ec69a1caa154858b36a04453a_0_6.json" --spreadsheet -p 28 -a 577.958,123.548,712.598,493.808 "fuji/HI-C655.pdf"
./scripts/tabula.sh -o "fuji/90fe6f0ec69a1caa154858b36a04453a_0_7.json" --spreadsheet -p 29 -a 90.653,134.258,293.378,531.293 "fuji/HI-C655.pdf"
./scripts/tabula.sh -o "fuji/90fe6f0ec69a1caa154858b36a04453a_0_8.json" --no-spreadsheet -p 29 -a 294.908,133.493,304.853,512.168 "fuji/HI-C655.pdf"
./scripts/tabula.sh -o "fuji/90fe6f0ec69a1caa154858b36a04453a_0_9.json" --spreadsheet -p 29 -a 306.383,127.373,396.653,498.398 "fuji/HI-C655.pdf"

