#!/bin/sh
set -x
set -e

#python process_json.py --input hitachi/lists.json --lists hitachi/lists.txt --run hitachi/run.sh
python process_json.py --dir hitachi
#python process_json.py --input hitachi/lists.json --lists hitachi/lists.txt
