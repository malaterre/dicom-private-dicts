#!/bin/sh
set -e
set -x
./tabula.sh -o "hitachi/page0.json" -p 57 -a 234.647,38.317,794.898,578.479 "hitachi/poc_013216.pdf"
#!/bin/sh
set -e
set -x
./tabula.sh -o "hitachi/page1.json" -p 58,64 "hitachi/poc_013216.pdf"
#!/bin/sh
set -e
set -x
./tabula.sh -o "hitachi/page2.json" -p 65 -a 54.686,44.269,123.88,568.807 "hitachi/poc_013216.pdf"
./tabula2xml.py  --owner "MMCPrivate" --use_table_header --files "hitachi/page0.json,hitachi/page1.json,hitachi/page2.json" --output "hitachi/poc_013216.xml"
