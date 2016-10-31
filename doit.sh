#!/bin/sh
set -x
set -e

python process_json.py --input hitachi/lists.json --lists hitachi/lists.txt --md5 hitachi/lists.md5
