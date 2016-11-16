#!/bin/sh
#set -x
set -e

dirs="agfa fuji gems hitachi other siemens"

for dir in $dirs
do
  echo "procesing dir: $dir"
  sh $dir/run2.sh
done
