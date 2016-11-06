#!/bin/sh
set -x
set -e

dirs="agfa fuji hitachi other"

for dir in $dirs
do
  python process_json.py --dir $dir
done

for dir in $dirs
do
  sh $dir/run.sh
done
