#!/bin/bash
#set -x
set -e
dirs="hitachi"
for d in $(ls -d $dirs)
do
  #echo $d
  #wget -c -i $i
  wget --quiet -t 1 -e robots=off -c --directory-prefix=$d -i $d/lists.txt
done

for d in $(ls -d $dirs)
do
  md5sum ${d}/*.pdf > ${d}/lists.md5
done

for d in $(ls -d $dirs)
do
  md5sum --quiet -c ${d}/lists.md5
done
echo "success"
