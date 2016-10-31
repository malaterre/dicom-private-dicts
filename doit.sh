#!/bin/sh
#set -x
set -e

dirs="agfa hitachi"

for dir in $dirs
do
  python process_json.py --dir $dir
done
